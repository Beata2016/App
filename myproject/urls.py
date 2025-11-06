from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('candidates/', include('candidates.urls', namespace='candidates')),
    path('jobs/', include('Ogloszeniafirm.urls', namespace='ogloszeniafirm')),  # ⬅️ Zmieniłem z 'vacatures/' na 'jobs/'
]