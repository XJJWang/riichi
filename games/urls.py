from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_record, name='add_record'),
]