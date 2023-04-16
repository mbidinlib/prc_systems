'''
This Python file defines all the views for the chatroom app
'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required  # Decorator to restrict some sessions 
from django.db.models import Q                              # Q is used to pass and/or statements which we will use to create the search filters
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User



# Create your views here.

# function to get values from loginpage post and authenticate
def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User Does not exist")
        # Note: Flash messages would be displayed on the main oage
        
        # Authenticate user and login
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, "Username or Password does not exists")
            
    context= {}
    return render(request, "chatroom/login_register.html",context )

# Logout
def logoutUser(request):
    logout(request)
    return redirect("home")





# This fnction defines the home view and 
# returns the location of the htlm file for hom 
# and other objecs that we want to see in the home 

def home(request):
    
    # Create a filter for selected topic or searched
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms =  Room.objects.filter(
        Q(topic__name__icontains=q) |    # There are other methods like __startswith __endswith
        Q(name__icontains=q)  |
        Q(description__icontains=q)  
        )
     
    topics =  Topic.objects.all()                                    # Gets all the topics in the models
    rooms_count = rooms.count()
    
    context = {'rooms': rooms, 'topics':topics, 'room_count':rooms_count}                      # additional values to retun for use in the home.html
    return render(request, 'chatroom/home.html', context)


'''#########################################
# This fnction defines the room view and 
# returns the location of the htlm file for room 
# and other objecs that we want to see in the home 
############################################'''
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}     
    return render(request, 'chatroom/room.html', context)


'''#########################################
# This fnction defines the create-room view 
# returns the location of the htlm file 
# and other objecs that we want to see in the home 
############################################'''


@login_required(login_url = "loginpage")             ## added a decorated to restrict those who are not loged in and redirect them to the login page
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        print(request.POST)     # this prints the details of a post into the comand line whe submitted
        
        # When a user creats a room, chck and see if all entries are valid, save the form
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()                   
            return redirect('home')  # and redirect to the home page
    
    context = {'form':form}
    return render(request, "chatroom/room_form.html", context)


# View to update room
def updateRoom(request, pk):
    room =  Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    
    # Flag and restrict users from updating other people's work
    if request.user != room.user:
        return HttpResponse("You cannot update a chat create by someone else")
    

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()                   
            return redirect('home')  # and redirect to the home page
    
    context = {'form':form}
    return render(request, 'chatroom/room_form.html', context)

# View that directs us the the generic delete html form
def deleteRoom(request, pk):
    room =  Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, "chatroom/delete.html", {'obj': room})