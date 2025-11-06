from django.urls import path
from . import views

app_name = 'candidates'  # ⬅️ TO JEST BARDZO WAŻNE!

urlpatterns = [
    path('', views.candidates_list, name='cv_base'),

]
