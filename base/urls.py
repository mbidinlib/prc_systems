from django.urls import path 
from . import views




# for the url pattern, we assign each pattern to a name so that we can reference the name.
# So that In cases that the url path changes, we don't have to change it in all forms
urlpatterns = [
    
    path('', views.home, name="home"),
    path('data_check/', views.data_check, name= "data_check"),
    path('data_visual/', views.data_visual, name= "data_visual"),
    path('data_engineer/', views.data_engineer, name= "data_engineer"),
    path('data_engineer/', views.other_systems, name= "data_other"),
    path('download/', views.download_file, name="download_file"),
    path('navigate/', views.navigate_to, name="navigate"),
    path('all_systems/', views.all_systems, name="systems"),
    
    # path("create-room/", views.createRoom, name='create-room'),  
    # path("update-room/<str:pk>/", views.updateRoom, name='update-room'),  
    # path("delete-room/<str:pk>/", views.deleteRoom, name='delete-room'),  
    # path("delete-message/<str:pk>/", views.deleteMessage, name='delete-message'),  

    #path("delete-room/<str:pk>/", views.deleteRoom, name='delete-room'),  
]
