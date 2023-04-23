from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatroom.urls')),
    path('api/', include('chatroom.api.urls'))
]