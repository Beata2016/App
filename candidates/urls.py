from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidates_list, name='candidates_list'),
]
