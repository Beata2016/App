from django.contrib import admin
from django.urls import path, include
from myapp import views  # TYLKO import widoków, bez modeli

urlpatterns = [
    path('admin/', admin.site.urls),
    path('candidates/', include('candidates.urls')),  # jeśli masz urls.py w aplikacji candidates
    path('jobs/', include('Ogloszeniafirm.urls')),   # jeśli masz urls.py w aplikacji Ogloszeniafirm
    path('', views.index, name='home'),              # Strona główna
    path('firma/', views.firma, name='firma'),
    path('overons/', views.overons, name='overons'),
    path('contact/', views.contactus, name='contactus'),
    path('ai_chat/', views.ai_chat, name='ai_chat'),
    path('cv/', views.cv_base, name='cv_base'),
    path('vacatures/', views.vacatures, name='vacatures'),
    path('voor_bedrijven/', views.voor_bedrijven, name='voor_bedrijven'),
]

