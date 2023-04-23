'''
This Python file defines all the views for the chatroom app
'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required  # Decorator to restrict some sessions 
from django.db.models import Q                              # Q is used to pass and/or statements which we will use to create the search filters
from .models import Room, Topic, Message
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm      # default user creation form in django. can be customized


# Create your views here.

# function to get values from loginpage post and authenticate
def loginPage(request):
    
    page = 'loginpage'
    
    # Prevent re-login by redirecting to home
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username').lower() 
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
            
    context= {'page': page}
    return render(request, "chatroom/login_register.html",context )


# Logout
def logoutUser(request):
    logout(request)
    return redirect("home")



def registerPage(request):
    
    # get the filled user and authenticate
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():                         # If the form is vali, we want to get the username
            user = form.save(commit=False)          # Don't save yet
            user.username = user.username.lower()   # Make username all lower
            user.save()                             # Save user
            
            # login user and redirect them to the home page
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occured during registration")
    
    form = UserCreationForm()
    context= {'form': form}
    return render(request, "chatroom/login_register.html", context)

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
    
    # Get messages for each room and filter by the topics
    room_messages =  Message.objects.filter(
        Q(room__topic__name__icontains=q)
    )   
    
    context = {'rooms': rooms, 'topics':topics, 'room_count':rooms_count,
               "room_messages": room_messages}                      # additional values to retun for use in the home.html
    return render(request, 'chatroom/home.html', context)


'''#########################################
# This fnction defines the room view and 
# returns the location of the htlm file for room 
# and other objecs that we want to see in the home 
############################################'''
def room(request, pk):
    room = Room.objects.get(id=pk)
    
    #Get all the items in the Message class in models for each room
    # var = room.[model_name - in lower caps].set.all()
    # This method can be used to get child values of all clases as in this case.
    room_messages = room.message_set.all()   
    
    participants = room.participants.all() # bring all the participants in the room and remember to add it to the context dictionary
    
    # Post cmments in a room
    if request.method == "POST":
        message =  Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')   # We are getting the body from the room.htlm comment-form
        )
        room.participants.add(request.user) # add the user to the room when the user commnets
        return redirect("room", pk=room.id)   # We could have avoided this but we put it here to ensure that if the post method is completed, we will remain in the same page
    
    context = {"room": room, 'room_messages': room_messages, "participants":participants}     
    return render(request, 'chatroom/room.html', context)


# User Profile view
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()         # all rooms the user is in
    room_messages = user.message_set.all()    # all messages the user is in
    topics = Topic.objects.all()            # all topics the user is in
    context = {'user':user, 'rooms':rooms, 'room_messages':room_messages, 'topics':topics}
    return render(request, 'chatroom/profile.html', context)
    




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
            
            room = form.save(commit= False)     # Partially saves the form and the next lines adds the host
            room.host = request.user      
            room.save()               
            return redirect('home')  # and redirect to the home page
    
    context = {'form':form}
    return render(request, "chatroom/room_form.html", context)


# View to update room
def updateRoom(request, pk):
    room =  Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    
    # Flag and restrict users from updating other people's work
    if request.user != room.host:
        return HttpResponse("You cannot update a chat create by someone else")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()                   
            return redirect('home')  # and redirect to the home page
    
    context = {'form':form}
    return render(request, 'chatroom/room_form.html', context)

# View that directs us the the generic delete html form
@login_required(login_url = "loginpage")             
def deleteRoom(request, pk):
    room =  Room.objects.get(id=pk)
    
        # Flag and restrict users from deleting other people's work
    if request.user != room.host:
        return HttpResponse("You cannot update a chat create by someone else")

    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, "chatroom/delete.html", {'obj': room})

# View to delet a message
@login_required(login_url = "loginpage")             
def deleteMessage(request, pk):
    message =  Message.objects.get(id=pk)
    
    # Flag and restrict users from deleting other people's Messages
    if request.user != message.user:
        return HttpResponse("You are not allowed to delete a message by someone else")

    if request.method == "POST":
        message.delete()
        return redirect('home')
    return render(request, "chatroom/delete.html", {'obj': message})


