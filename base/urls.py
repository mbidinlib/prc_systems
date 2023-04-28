from django.urls import path 
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.Home, name="home"),
    path('data_check/', views.DataCheck, name= "data_check"),
    
    path('data_visual/', views.DataVisual, name= "data_visual"),

    path('data_engineer/', views.DataEngineer, name= "data_engineer"),
    path('data_engineer/', views.OtherSystems, name= "data_other"),
    path('download/', views.DownloadFile, name="download_file"),
    path('navigate/', views.NavigateTo, name="navigate"),
    path('all_systems/', views.AllSystems, name="systems"),
    path('myprofile/', views.MyProfile, name="myprofile"),
    ]
