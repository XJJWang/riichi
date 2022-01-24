from django.contrib import admin
from django.urls import include, path
from games import views

urlpatterns = [
    path('games/', include('games.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]
