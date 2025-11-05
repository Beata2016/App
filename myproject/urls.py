from django.contrib import admin
from django.urls import path, include
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # strona główna
    path('app/ogloszenia/', include('Ogloszeniafirm.urls')),
    path('app/baza-danych/', include('candidates.urls')),
]

