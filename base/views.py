'''
This Python file defines all the views for the chatroom app
'''
import os
import mimetypes
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
systems = [
    {'id': 1, 'name': 'Data Check System', 'det':
        '''PRC Data Check System (PRCDC) is a Python based GUI app for checking and processing data. 
          The app currently comes with three main functionalities that invludes; general data checks, API data download, 
          data dictionary for ODK related surveys ...   ''',
        'img' : 'prcdc.png',
        'link' : 'data_check'

    },
    
    {'id': 2, 'name': 'Data Visualization',     
     'det': '''An interactive Online system for data visualization. 
     Import your data in a CSV or XLS/XLSX formats and select the visualization type that suits your needs.  ''',
     'img' : '',
     'link' : 'data_visual'
    },
    
    {'id': 3, 'name': 'Data Engineer',
     'det': '''An Online system for cheking and preparing your data for analysis. 
     This is essentially the online version of the installable Data check system''',
    
     'img' : '',
     'link' : 'data_engineer'  
     
     },


    {'id': 4, 'name': 'Other Systems',
     'det': 'Other Systems',
     'img' : '',
     'link' : 'other_systems'

     }

]


def home(request):
    
    context = {'systems': systems}
    return render(request, 'base/home.html', context)


def data_check(request):

    context = {'systems': systems}
    return render(request, 'base/data_check.html', context)


def data_visual(request):

    context = {'systems': systems}
    return render(request, 'base/data_visual.html', context)


def data_engineer(request):

    context = {'systems': systems}
    return render(request, 'base/data_engineer.html', context)


def other_systems(request):

    context = {'systems': systems}
    return render(request, 'base/other_systems.html', context)



# Define function to download file using template
def download_file(request, filename=''):
    
    filename =  request.GET.get('filename')
    print(filename)
    
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/files/exe/' + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        # Load the template
        return render(request, 'base/home.html')