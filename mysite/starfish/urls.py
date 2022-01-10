from django.urls import path

from . import views

urlpatterns = [
    path('', views.starfish, name='starfish'),
]
