from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('candidates/', include('candidates.urls', namespace='candidates')),
     path('vacatures/', include('Ogloszeniafirm.urls', namespace='ogloszeniafirm')),  # używamy namespace zgodnego z app_name
]
