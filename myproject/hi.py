hi

Hello! How can I help you today?

ten link musze zmienic na  te zdjecie pomoz mi background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url(''{% static 'app_name/images/foto 1 (1).jpg' %}'') center/cover;
            min-height: 500px;

Widzę, że chcesz zmienić gradient na zdjęcie w tle. Pomogę Ci!

Żeby zamienić background: linear-gradient(...) na zdjęcie z Django static files, wystarczy zmienić tę linię na:

css
background: url('{% static "app_name/images/foto 1 (1).jpg" %}') center/cover;
min-height: 500px;
Albo jeśli chcesz zachować ciemny overlay (gradient) NA WIERZCHU zdjęcia, użyj:

css
background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('{% static "app_name/images/foto 1 (1).jpg" %}') center/cover;
min-height: 500px;
Ważne:

Zamień app_name na rzeczywistą nazwę Twojej aplikacji Django
Upewnij się, że plik foto 1 (1).jpg znajduje się w folderze app_name/static/app_name/images/
Na górze pliku HTML/template musi być {% load static %}
Którą wersję preferujesz - ze zdjęciem samym czy z ciemnym overlayem?


      .hero-image {
          background: url('{% static "app_name/images/foto 1 (1).jpg" %}') center/cover;
          min-height: 500px;
        }
Świetnie! Twój kod wygląda dobrze. Pamiętaj tylko o kilku rzeczach, żeby zadziałało:

Na początku pliku HTML dodaj:
html
{% load static %}
Zamień app_name na nazwę swojej aplikacji Django, np.:
css
.hero-image {
    background: url('{% static "myapp/images/foto 1 (1).jpg" %}') center/cover;
    min-height: 500px;
}
```

3. **Struktura folderów powinna wyglądać tak:**
```
myapp/
└── static/
    └── myapp/
        └── images/
            └── foto 1 (1).jpg
W HTML użyj tej klasy:
html
<div class="hero-image">
    <!-- Twoja treść -->
</div>
Ewentualnie dodaj dodatkowe właściwości dla lepszego efektu:
css
.hero-image {
    background: url('{% static "app_name/images/foto 1 (1).jpg" %}') center/cover;
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    min-height: 500px;
}
Jeśli zdjęcie się nie wyświetla, sprawdź:

Czy uruchomiłeś python manage.py collectstatic (w produkcji)
Czy nazwa aplikacji jest poprawna
Czy plik rzeczywiście istnieje w tym folderze
Potrzebujesz jeszcze pomocy z czymś?


zdjecie sie nie wyswitla

Dobra, sprawdźmy co może być nie tak. Przejdźmy krok po kroku:

1. Sprawdź czy masz {% load static %} na górze pliku
html
{% load static %}
<!DOCTYPE html>
<html>
...
```

## 2. Sprawdź strukturę folderów
Jaka jest nazwa Twojej aplikacji Django? Struktura powinna być:
```
nazwa_twojej_aplikacji/
└── static/
    └── nazwa_twojej_aplikacji/
        └── images/
            └── foto 1 (1).jpg
3. Sprawdź settings.py
Upewnij się, że masz:

python
STATIC_URL = '/static/'
4. Tymczasowo przetestuj ze zdjęciem z internetu
Żeby sprawdzić czy problem jest w ścieżce, zamień na:

css
.hero-image {
    background: url('https://picsum.photos/1200/500') center/cover;
    min-height: 500px;
}
Jeśli to zadziała, to problem jest w ścieżce do pliku lokalnego.

5. Spróbuj alternatywnej składni
css
.hero-image {
    background-image: url('{% static "app_name/images/foto 1 (1).jpg" %}');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    min-height: 500px;
}
Możesz mi wysłać:

Nazwę swojej aplikacji Django?
Gdzie dokładnie masz ten CSS (inline w HTML czy w osobnym pliku .css)?
Screenshot lub dokładną ścieżkę do pliku ze zdjęciem?
To pomoże mi lepiej Ci pomóc! 🔍


bylo tak chce zwykle zdjecie  .hero-image {             background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1200') center/cover;             min-height: 500px;         }  foto 1 (1).jpg" %}'

Aha, rozumiem! Chcesz zamienić link z Unsplash na swoje lokalne zdjęcie.

Zmień to tak:

css
.hero-image {
    background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{% static "app_name/images/foto 1 (1).jpg" %}') center/cover;
    min-height: 500px;
}
ALE UWAGA! Jeśli ten CSS jest w osobnym pliku .css, to składnia Django {% static %} nie zadziała! Django przetwarza tylko pliki .html.

Masz 2 opcje:
Opcja 1: CSS inline w pliku HTML (DZIAŁA)
html
{% load static %}

<style>
    .hero-image {
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{% static "app_name/images/foto 1 (1).jpg" %}') center/cover;
        min-height: 500px;
    }
</style>

<div class="hero-image">
    <!-- treść -->
</div>
Opcja 2: Osobny plik CSS (użyj pełnej ścieżki)
css
/* style.css */
.hero-image {
    background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('/static/app_name/images/foto 1 (1).jpg') center/cover;
    min-height: 500px;
}
Pamiętaj:

Zamień app_name na nazwę swojej aplikacji
Upewnij się, że plik jest w: app_name/static/app_name/images/foto 1 (1).jpg
Gdzie masz teraz ten CSS - w pliku HTML czy w osobnym .css?



<!DOCTYPE html> <html lang="pl"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>HR Partner - O nas</title> <script src="https://cdn.tailwindcss.com"></script> <link rel="stylesheet" href="https://cdnjs.cloudfla

pasted

wsadz ta fotke tylko

Widzę problem! Masz zwykły HTML (nie Django template), więc składnia {% static %} nie zadziała.

Zrobiłem Ci poprawioną wersję - po prostu wstaw swoją ścieżkę do zdjęcia:

HR Partner - O nas (ze zdjęciem)
Interactive artifact 
Gotowe!

Teraz musisz tylko:

Umieścić plik foto 1 (1).jpg w tym samym folderze co plik HTML
Albo zmienić nazwę w linii 36 na właściwą ścieżkę do Twojego zdjęcia:
css
background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('TUTAJ_TWOJA_ŚCIEŻKA') center/cover;
Możliwe ścieżki:

foto-1-(1).jpg - jeśli plik jest w tym samym folderze
images/foto-1-(1).jpg - jeśli plik jest w podfolderze images
/static/images/foto-1-(1).jpg - jeśli używasz struktury ze static
Tip: Zmień nazwę pliku na coś prostszego bez spacji i nawiasów, np. foto1.jpg - będzie łatwiej!


poprosze zrob mi ta  strone  aby  dzialala  w djanbgo z  baza  danych mam  dwi e  Ogloszenia Firm  lub candidates doloz  naglowii tlumaczenie strony na inne  jezyki  i stopke z  socjal media i  chat  ten tani darmowy

Django HR Partner - Kompletny Projekt
Code ∙ Version 2 
Gotowe! Stworzyłem dla Ciebie kompletny projekt Django z:

✅ Bazą danych:

Model Candidate (kandydaci z CV)
Model JobOffer (ogłoszenia firm)
✅ Panel admina - możesz dodawać oferty i kandydatów

✅ Wielojęzyczność:

Polski, Holenderski, Angielski, Czeski, Bułgarski
Przełączanie języków w nagłówku
System tłumaczeń Django
✅ Stopka ze social media:

Facebook, Twitter, LinkedIn, Instagram
✅ DARMOWY CHAT - Tawk.to:

100% darmowy live chat
Bez limitów wiadomości
Aplikacja mobilna dla obsługi
Jak zainstalować:
bash
# 1. Zainstaluj pakiety
pip install Django Pillow django-rosetta

# 2. Utwórz projekt
django-admin startproject hrpartner_project
cd hrpartner_project
python manage.py startapp hrpartner

# 3. Skopiuj kod z artyfaktu do plików

# 4. Migruj bazę
python manage.py makemigrations
python manage.py migrate

# 5. Utwórz admina
python manage.py createsuperuser

# 6. Uruchom
python manage.py runserver
Darmowy chat Tawk.to:
Zarejestruj się → https://www.tawk.to
Skopiuj swój Widget Code
Wklej do base.html (jest tam komentarz gdzie)
Masz pytania jak to uruchomić? 🚀









# ==== 1. models.py ====
from django.db import models
from django.utils.translation import gettext_lazy as _

class Candidate(models.Model):
    LANGUAGE_CHOICES = [
        ('pl', 'Polski'),
        ('nl', 'Nederlands'),
        ('en', 'English'),
        ('cs', 'Čeština'),
        ('bg', 'Български'),
    ]
    
    first_name = models.CharField(_('Imię'), max_length=100)
    last_name = models.CharField(_('Nazwisko'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Telefon'), max_length=20)
    cv_file = models.FileField(_('CV'), upload_to='cvs/', blank=True, null=True)
    photo = models.ImageField(_('Zdjęcie'), upload_to='candidates/', blank=True, null=True)
    position = models.CharField(_('Stanowisko'), max_length=200)
    experience_years = models.IntegerField(_('Lata doświadczenia'), default=0)
    languages = models.CharField(_('Języki'), max_length=50, choices=LANGUAGE_CHOICES)
    skills = models.TextField(_('Umiejętności'))
    description = models.TextField(_('Opis'), blank=True)
    available = models.BooleanField(_('Dostępny'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Kandydat')
        verbose_name_plural = _('Kandydaci')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class JobOffer(models.Model):
    SECTOR_CHOICES = [
        ('construction', _('Budownictwo')),
        ('production', _('Produkcja')),
        ('agriculture', _('Rolnictwo')),
        ('it', _('IT')),
        ('logistics', _('Logistyka')),
        ('finance', _('Finanse')),
        ('healthcare', _('Opieka zdrowotna')),
    ]
    
    title = models.CharField(_('Tytuł'), max_length=200)
    company_name = models.CharField(_('Nazwa firmy'), max_length=200)
    company_logo = models.ImageField(_('Logo firmy'), upload_to='companies/', blank=True, null=True)
    sector = models.CharField(_('Sektor'), max_length=50, choices=SECTOR_CHOICES)
    location = models.CharField(_('Lokalizacja'), max_length=200)
    salary_min = models.DecimalField(_('Wynagrodzenie od'), max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(_('Wynagrodzenie do'), max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(_('Opis stanowiska'))
    requirements = models.TextField(_('Wymagania'))
    benefits = models.TextField(_('Benefity'), blank=True)
    contract_type = models.CharField(_('Typ umowy'), max_length=100)
    is_active = models.BooleanField(_('Aktywna'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Ogłoszenie')
        verbose_name_plural = _('Ogłoszenia')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.company_name}"


# ==== 2. admin.py ====
from django.contrib import admin
from .models import Candidate, JobOffer

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'experience_years', 'available', 'created_at')
    list_filter = ('available', 'languages', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'position', 'skills')
    list_editable = ('available',)

@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'sector', 'location', 'is_active', 'created_at')
    list_filter = ('is_active', 'sector', 'created_at')
    search_fields = ('title', 'company_name', 'description')
    list_editable = ('is_active',)


# ==== 3. views.py ====
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Candidate, JobOffer

def home(request):
    recent_jobs = JobOffer.objects.filter(is_active=True)[:6]
    return render(request, 'hrpartner/home.html', {'recent_jobs': recent_jobs})

def about(request):
    return render(request, 'hrpartner/about.html')

class JobListView(ListView):
    model = JobOffer
    template_name = 'hrpartner/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = JobOffer.objects.filter(is_active=True)
        sector = self.request.GET.get('sector')
        if sector:
            queryset = queryset.filter(sector=sector)
        return queryset

class JobDetailView(DetailView):
    model = JobOffer
    template_name = 'hrpartner/job_detail.html'
    context_object_name = 'job'

class CandidateListView(ListView):
    model = Candidate
    template_name = 'hrpartner/candidate_list.html'
    context_object_name = 'candidates'
    paginate_by = 12
    
    def get_queryset(self):
        return Candidate.objects.filter(available=True)

class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'hrpartner/candidate_detail.html'
    context_object_name = 'candidate'

def contact(request):
    return render(request, 'hrpartner/contact.html')


# ==== 4. urls.py ====
from django.urls import path
from . import views

app_name = 'hrpartner'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('candidates/', views.CandidateListView.as_view(), name='candidate_list'),
    path('candidates/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
    path('contact/', views.contact, name='contact'),
]


# ==== 5. settings.py (FRAGMENTY DO DODANIA) ====
"""
INSTALLED_APPS = [
    ...
    'hrpartner',
    'rosetta',  # Do zarządzania tłumaczeniami w adminie
]

MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
]

LANGUAGES = [
    ('pl', 'Polski'),
    ('nl', 'Nederlands'),
    ('en', 'English'),
    ('cs', 'Čeština'),
    ('bg', 'Български'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

LANGUAGE_CODE = 'pl'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# W głównym urls.py dodaj:
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('hrpartner.urls')),
    path('rosetta/', include('rosetta.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""


# ==== 6. base.html ====
"""
{% load static %}
{% load i18n %}
<!DOCTYPE html>
<html lang="{{ LANGUAGE_CODE }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}HR Partner{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .hero-image {
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                        url('{% static "hrpartner/images/hero.jpg" %}') center/cover;
            min-height: 500px;
        }
    </style>
</head>
<body class="bg-gray-50">
    <!-- Header/Navbar -->
    <header class="fixed w-full bg-white shadow-md z-50">
        <div class="max-w-7xl mx-auto px-4 py-4">
            <div class="flex justify-between items-center">
                <a href="{% url 'hrpartner:home' %}" class="text-2xl font-bold text-blue-600">
                    HR Partner
                </a>
                
                <nav class="hidden md:flex gap-6 text-sm">
                    <a href="{% url 'hrpartner:home' %}" class="hover:text-blue-600">{% trans "Strona główna" %}</a>
                    <a href="{% url 'hrpartner:about' %}" class="hover:text-blue-600">{% trans "O nas" %}</a>
                    <a href="{% url 'hrpartner:job_list' %}" class="hover:text-blue-600">{% trans "Oferty pracy" %}</a>
                    <a href="{% url 'hrpartner:candidate_list' %}" class="hover:text-blue-600">{% trans "Kandydaci" %}</a>
                    <a href="{% url 'hrpartner:contact' %}" class="hover:text-blue-600">{% trans "Kontakt" %}</a>
                </nav>
                
                <!-- Zmiana języka -->
                <div class="flex gap-2">
                    {% get_current_language as LANGUAGE_CODE %}
                    {% get_available_languages as LANGUAGES %}
                    {% for lang_code, lang_name in LANGUAGES %}
                        <form action="{% url 'set_language' %}" method="post" style="display: inline;">
                            {% csrf_token %}
                            <input name="next" type="hidden" value="{{ request.path }}" />
                            <input name="language" type="hidden" value="{{ lang_code }}" />
                            <button type="submit" class="px-3 py-1 rounded {% if LANGUAGE_CODE == lang_code %}bg-blue-600 text-white{% else %}bg-gray-200{% endif %}">
                                {{ lang_code|upper }}
                            </button>
                        </form>
                    {% endfor %}
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="pt-20">
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-300 py-12 mt-20">
        <div class="max-w-7xl mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8 mb-8">
                <div>
                    <h3 class="text-xl font-bold text-white mb-4">HR Partner</h3>
                    <p class="text-sm">{% trans "Wiodąca agencja rekrutacyjna w Holandii" %}</p>
                </div>
                
                <div>
                    <h4 class="font-semibold text-white mb-4">{% trans "Szybkie linki" %}</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="{% url 'hrpartner:home' %}" class="hover:text-white">{% trans "Strona główna" %}</a></li>
                        <li><a href="{% url 'hrpartner:about' %}" class="hover:text-white">{% trans "O nas" %}</a></li>
                        <li><a href="{% url 'hrpartner:job_list' %}" class="hover:text-white">{% trans "Oferty pracy" %}</a></li>
                        <li><a href="{% url 'hrpartner:candidate_list' %}" class="hover:text-white">{% trans "Kandydaci" %}</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="font-semibold text-white mb-4">{% trans "Kontakt" %}</h4>
                    <ul class="space-y-2 text-sm">
                        <li><i class="fas fa-phone mr-2"></i> +31 123 456 789</li>
                        <li><i class="fas fa-envelope mr-2"></i> info@hrpartner.nl</li>
                        <li><i class="fas fa-map-marker-alt mr-2"></i> Amsterdam, NL</li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="font-semibold text-white mb-4">{% trans "Social Media" %}</h4>
                    <div class="flex gap-4 text-2xl">
                        <a href="#" class="hover:text-blue-400"><i class="fab fa-facebook"></i></a>
                        <a href="#" class="hover:text-blue-300"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="hover:text-blue-600"><i class="fab fa-linkedin"></i></a>
                        <a href="#" class="hover:text-pink-400"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
            </div>
            
            <div class="border-t border-gray-800 pt-8 text-center text-sm">
                <p>&copy; 2025 HR Partner. {% trans "Wszelkie prawa zastrzeżone." %}</p>
            </div>
        </div>
    </footer>

    <!-- Tawk.to Chat (DARMOWY) -->
    <script type="text/javascript">
    var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
    (function(){
        var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
        s1.async=true;
        s1.src='https://embed.tawk.to/TWOJ_ID_TUTAJ/default';
        s1.charset='UTF-8';
        s1.setAttribute('crossorigin','*');
        s0.parentNode.insertBefore(s1,s0);
    })();
    </script>
</body>
</html>
"""


# ==== 7. about.html ====
"""
{% extends 'hrpartner/base.html' %}
{% load static %}
{% load i18n %}

{% block title %}{% trans "O nas" %} - HR Partner{% endblock %}

{% block content %}
<section class="hero-image flex items-center justify-center">
    <div class="max-w-4xl mx-auto text-center text-white px-4">
        <h1 class="text-5xl md:text-6xl font-bold mb-6">{% trans "Poznaj naszą misję" %}</h1>
        <p class="text-xl">{% trans "20 lat doświadczenia w rekrutacji" %}</p>
    </div>
</section>

<section class="py-20 px-4">
    <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-12">
        <div class="bg-white rounded-xl p-8 shadow-lg">
            <h3 class="text-3xl font-bold mb-4 text-gray-900">{% trans "Nasza misja" %}</h3>
            <p class="text-gray-700">{% trans "Łączymy najlepsze talenty z wiodącymi firmami w Holandii" %}</p>
        </div>
        <div class="bg-white rounded-xl p-8 shadow-lg">
            <h3 class="text-3xl font-bold mb-4 text-gray-900">{% trans "Nasza wizja" %}</h3>
            <p class="text-gray-700">{% trans "Być liderem w rekrutacji i doradztwie kariery" %}</p>
        </div>
    </div>
</section>
{% endblock %}
"""


# ==== 8. job_list.html ====
"""
{% extends 'hrpartner/base.html' %}
{% load i18n %}

{% block title %}{% trans "Oferty pracy" %} - HR Partner{% endblock %}

{% block content %}
<div class="max-w-7xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold mb-8">{% trans "Aktualne oferty pracy" %}</h1>
    
    <!-- Filtry -->
    <div class="mb-8">
        <form method="get" class="flex gap-4">
            <select name="sector" class="px-4 py-2 border rounded-lg">
                <option value="">{% trans "Wszystkie sektory" %}</option>
                <option value="construction">{% trans "Budownictwo" %}</option>
                <option value="production">{% trans "Produkcja" %}</option>
                <option value="it">IT</option>
                <option value="logistics">{% trans "Logistyka" %}</option>
            </select>
            <button type="submit" class="bg-blue-600 text-white px-6 py-2 rounded-lg">{% trans "Filtruj" %}</button>
        </form>
    </div>
    
    <!-- Lista ofert -->
    <div class="grid md:grid-cols-3 gap-6">
        {% for job in jobs %}
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition">
            {% if job.company_logo %}
                <img src="{{ job.company_logo.url }}" alt="{{ job.company_name }}" class="h-16 mb-4">
            {% endif %}
            <h3 class="text-xl font-bold mb-2">{{ job.title }}</h3>
            <p class="text-gray-600 mb-2">{{ job.company_name }}</p>
            <p class="text-sm text-gray-500 mb-4">
                <i class="fas fa-map-marker-alt"></i> {{ job.location }}
            </p>
            {% if job.salary_min %}
            <p class="text-green-600 font-semibold mb-4">
                €{{ job.salary_min }} - €{{ job.salary_max }}
            </p>
            {% endif %}
            <a href="{% url 'hrpartner:job_detail' job.pk %}" 
               class="block text-center bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700">
                {% trans "Zobacz szczegóły" %}
            </a>
        </div>
        {% empty %}
        <p class="col-span-3 text-center text-gray-500">{% trans "Brak ofert" %}</p>
        {% endfor %}
    </div>
    
    <!-- Paginacja -->
    {% if is_paginated %}
    <div class="mt-8 flex justify-center gap-2">
        {% if page_obj.has_previous %}
        <a href="?page=1" class="px-4 py-2 bg-gray-200 rounded">{% trans "Pierwsza" %}</a>
        <a href="?page={{ page_obj.previous_page_number }}" class="px-4 py-2 bg-gray-200 rounded">{% trans "Poprzednia" %}</a>
        {% endif %}
        
        <span class="px-4 py-2">{{ page_obj.number }} / {{ page_obj.paginator.num_pages }}</span>
        
        {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}" class="px-4 py-2 bg-gray-200 rounded">{% trans "Następna" %}</a>
        <a href="?page={{ page_obj.paginator.num_pages }}" class="px-4 py-2 bg-gray-200 rounded">{% trans "Ostatnia" %}</a>
        {% endif %}
    </div>
    {% endif %}
</div>
{% endblock %}
"""
