'''
This Python file defines all the views for the chatroom app
'''
import os
import json
import pandas as pd
import openpyxl
import mimetypes
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Datasets
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings

from .file_form import FileForm
 


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


def Home(request):
    
    context = {'systems': systems}
    return render(request, 'base/home.html', context)


def DataCheck(request):

    context = {'systems': systems}
    return render(request, 'base/data_check.html', context)



def AddDataset(request):
    datasets = Datasets.objects.all()
    context = {'systems': systems, 'dataset': datasets}
    return render(request, 'base/data_visual.html', context)



def DataEngineer(request):

    context = {'systems': systems}
    return render(request, 'base/data_engineer.html', context)


def OtherSystems(request):

    context = {'systems': systems}
    return render(request, 'base/other_systems.html', context)


# Define function to download file using template
def DownloadFile(request, filename=''):
    
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


# Navigate to
def NavigateTo(request):
    context = {'systems': systems}
    return render(request, 'base/activity.html', context)


def AllSystems(request):
    context = {'systems': systems}
    return render(request, 'base/systems.html', context)


def MyProfile(request):
    context = {'systems': systems}
    return render(request, 'base/profile.html', context)



# Data visualization view
########################
def DataVisual(request):
    fileform = FileForm()
    
    if request.method == 'POST':
        fileform = FileForm(request.POST, request.FILES)
        if fileform.is_valid():
            formdata=fileform.cleaned_data 
            #fileform.save(commit=False)

            file =formdata["file"]
            name = formdata["name"]
            filename = str(file)
                        
        #Process data
        file_ext = str(filename).split(".")[-1].lower()
        if name is None:
            name = str(filename).split(".")[0]
        # filepath = (settings.UPLOAD_FOLDER + "/" + file).replace("//", "/").replace("\\", "/")
        
        # Read CSVs
        if file_ext == 'csv':
            df = pd.read_csv(file)
            data = df.to_json()
        
        # Read file with XLS/XLSX formats
        elif file_ext == 'xlsx' or file_ext == 'xls':
            df = pd.read_excel(file,engine='openpyxl')
            data = df.to_json()

        #Create object for the dataset and ignore the file file before saving
        f_form = Datasets.objects.create(name=request.POST['name'], file=None, data=data)
        f_form.save() 
                 
        #Finalize items in the context dictionary
        html_data = df.to_html(index=False)
        
        print(data)
        
        context = {'systems': systems, 'fileform': fileform, "data": html_data, "filename": name}
        
    else:
        context = {'systems': systems, 'fileform': fileform}        

    return render(request, 'base/data_visual.html', context)
