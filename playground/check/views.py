from django.shortcuts import render

# Create your views here.



section = [
    {'id':1, "name":"section1"}, 
    {'id':2, "name":"section2"}, 
    {'id':3, "name":"section3"}, 

]


def home(request):
    context = {'section': section}
    return render(request, 'check/home.html', context)


def guide(request):
    return render(request, 'check/guide.html')

