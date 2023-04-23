from django.urls import path
from . import views



# for the url pattern, we assign each pattern to a name so that we can reference the name.
# So that In cases that the url path changes, we don't have to change it in all forms
urlpatterns = [
    path('login/',views.loginPage, name="loginpage"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),

    
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name= "room"),
    path('profile/<str:pk>/', views.userProfile, name= "user-profile"),
    
    path("create-room/", views.createRoom, name='create-room'),  
    path("update-room/<str:pk>/", views.updateRoom, name='update-room'),  
    path("delete-room/<str:pk>/", views.deleteRoom, name='delete-room'),  
    path("delete-message/<str:pk>/", views.deleteMessage, name='delete-message'),  

    #path("delete-room/<str:pk>/", views.deleteRoom, name='delete-room'),  

]