from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from django.conf.urls import url

from games import views
from . import settings

urlpatterns = [
    path('games/', include('games.urls')),
    path('admin/', admin.site.urls),
    path('rankings/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT }),

]
