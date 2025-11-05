from django.urls import path
from .views import candidates_list

urlpatterns = [
    path('', candidates_list, name='candidates_list'),
]
