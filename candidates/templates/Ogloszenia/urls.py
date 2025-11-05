# ogloszeniafirm/urls.py

from django.urls import path
from . import views

app_name = 'ogloszeniafirm'

urlpatterns = [
    path('', views.job_list, name='job_list'),  # Lista ofert + AI chat
]
