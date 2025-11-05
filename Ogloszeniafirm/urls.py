# ogloszeniafirm/urls.py

from django.urls import path
from . import views

app_name = 'ogloszeniafirm'

urlpatterns = [
    path('', views.job_list, name='job_list'),  # Lista ofert + AI chat
    path('api/jobs/', views.jobs_api, name='jobs_api'),
    path('api/jobs/<int:job_id>/', views.job_detail_api, name='job_detail_api'),
]
