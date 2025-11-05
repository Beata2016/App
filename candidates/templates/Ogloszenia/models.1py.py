# ==== 1. models.py (DODAJ DO ISTNIEJĄCYCH MODELI) ====
from django.db import models
from django.utils.translation import gettext_lazy as _

class Candidate(models.Model):
    LANGUAGE_CHOICES = [
        ('pl', 'Polski'),
        ('nl', 'Nederlands'),
        ('en', 'English'),
        ('cs', 'Čeština'),
        ('bg', 'Български'),
        ('de', 'Deutsch'),
        ('ru', 'Русский'),
    ]
    
    INDUSTRY_CHOICES = [
        ('construction', _('Budownictwo')),
        ('production', _('Produkcja')),
        ('logistics', _('Logistyka')),
        ('technical', _('Techniczne')),
        ('cleaning', _('Sprzątanie')),
        ('other', _('Inne')),
    ]
    
    # Podstawowe info
    code = models.CharField(_('Kod kandydata'), max_length=20, unique=True)
    position = models.CharField(_('Stanowisko'), max_length=200)
    age = models.IntegerField(_('Wiek'), null=True, blank=True)
    
    # Lokalizacja
    country = models.CharField(_('Kraj'), max_length=100, default='Poland')
    city = models.CharField(_('Miasto'), max_length=100, blank=True)
    
    # Doświadczenie
    experience_years = models.IntegerField(_('Lata doświadczenia'), default=0)
    industry = models.CharField(_('Branża'), max_length=50, choices=INDUSTRY_CHOICES, default='other')
    
    # CV i dokumenty
    cv_file = models.FileField(_('CV'), upload_to='cvs/', blank=True, null=True)
    photo = models.ImageField(_('Zdjęcie'), upload_to='candidates/', blank=True, null=True)
    
    # Umiejętności
    skills = models.TextField(_('Umiejętności'), blank=True)
    languages_spoken = models.CharField(_('Języki'), max_length=50, choices=LANGUAGE_CHOICES)
    
    # Status
    available = models.BooleanField(_('Dostępny'), default=True)
    worked_in_nl = models.BooleanField(_('Pracował w NL'), default=False)
    worked_in_eu = models.BooleanField(_('Pracował w EU'), default=False)
    
    # Dodatkowe
    description = models.TextField(_('Opis'), blank=True)
    tags = models.CharField(_('Tagi'), max_length=500, blank=True, help_text='Oddzielone przecinkami')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Kandydat')
        verbose_name_plural = _('Kandydaci')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.code} - {self.position}"
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


# ==== 2. admin.py (DODAJ) ====
from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('code', 'position', 'age', 'city', 'country', 'experience_years', 'available', 'created_at')
    list_filter = ('available', 'worked_in_nl', 'worked_in_eu', 'industry', 'country')
    search_fields = ('code', 'position', 'city', 'country', 'skills', 'tags')
    list_editable = ('available',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Podstawowe informacje', {
            'fields': ('code', 'position', 'age', 'photo')
        }),
        ('Lokalizacja', {
            'fields': ('country', 'city')
        }),
        ('Doświadczenie', {
            'fields': ('experience_years', 'industry', 'skills', 'languages_spoken', 'tags')
        }),
        ('Status', {
            'fields': ('available', 'worked_in_nl', 'worked_in_eu')
        }),
        ('Dokumenty', {
            'fields': ('cv_file', 'description')
        }),
        ('Daty', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ==== 3. views.py (DODAJ) ====
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Candidate

def candidate_database(request):
    """Główna strona z bazą kandydatów"""
    candidates = Candidate.objects.filter(available=True)
    
    # Filtry
    search_query = request.GET.get('search', '')
    filter_type = request.GET.get('filter', 'all')
    
    if search_query:
        candidates = candidates.filter(
            Q(position__icontains=search_query) |
            Q(city__icontains=search_query) |
            Q(country__icontains=search_query) |
            Q(tags__icontains=search_query) |
            Q(industry__icontains=search_query)
        )
    
    if filter_type == 'available':
        candidates = candidates.filter(available=True)
    elif filter_type == 'nl':
        candidates = candidates.filter(worked_in_nl=True)
    elif filter_type == 'eu':
        candidates = candidates.filter(worked_in_eu=True)
    elif filter_type == 'construction':
        candidates = candidates.filter(
            Q(industry='construction') | Q(tags__icontains='construction')
        )
    elif filter_type == 'production':
        candidates = candidates.filter(
            Q(industry='production') | Q(tags__icontains='production')
        )
    
    context = {
        'candidates': candidates,
        'search_query': search_query,
        'filter_type': filter_type,
        'total_count': candidates.count()
    }
    
    return render(request, 'hrpartner/candidate_database.html', context)


class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'hrpartner/candidate_detail.html'
    context_object_name = 'candidate'


# ==== 4. urls.py (DODAJ DO ISTNIEJĄCYCH) ====
from django.urls import path
from . import views

app_name = 'hrpartner'

urlpatterns = [
    # ... istniejące URL
    path('candidates-db/', views.candidate_database, name='candidate_database'),
    path('candidates-db/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
]


# ==== 5. candidate_database.html ====
"""
{% extends 'hrpartner/base.html' %}
{% load static %}
{% load i18n %}

{% block title %}{% trans "Baza Kandydatów" %} - HR Partner{% endblock %}

{% block extra_css %}
<style>
    .hero-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 80px 30px;
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
    }

    .hero-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: moveGrid 20s linear infinite;
    }

    @keyframes moveGrid {
        0% { transform: translate(0, 0); }
        100% { transform: translate(50px, 50px); }
    }

    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 800px;
        margin: 0 auto;
    }

    .search-section {
        max-width: 1200px;
        margin: -40px auto 40px;
        padding: 0 30px;
        position: relative;
        z-index: 10;
    }

    .search-card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }

    .search-input-wrapper {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
    }

    .search-input {
        flex: 1;
        padding: 18px 25px;
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        font-size: 16px;
    }

    .search-input:focus {
        outline: none;
        border-color: #667eea;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
    }

    .search-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 18px 40px;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .search-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }

    .quick-filters {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }

    .quick-filter-btn {
        padding: 10px 20px;
        background: #f0f0f0;
        border: 2px solid transparent;
        border-radius: 25px;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.3s ease;
        text-decoration: none;
        color: #333;
        display: inline-block;
    }

    .quick-filter-btn:hover, .quick-filter-btn.active {
        background: white;
        border-color: #667eea;
        color: #667eea;
    }

    .candidates-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 25px;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 30px 60px;
    }

    .candidate-card {
        background: white;
        border: 2px solid #f0f0f0;
        border-radius: 15px;
        padding: 25px;
        transition: all 0.3s ease;
        cursor: pointer;
        text-align: center;
    }

    .candidate-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
    }

    .candidate-avatar {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2.2em;
        font-weight: 700;
        margin: 0 auto 15px;
        text-transform: uppercase;
    }

    .candidate-code {
        font-size: 1.2em;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 10px;
    }

    .candidate-position {
        font-size: 1.1em;
        font-weight: 600;
        color: #333;
        margin-bottom: 15px;
        min-height: 50px;
    }

    .candidate-info {
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-bottom: 15px;
    }

    .info-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 12px;
        background: #f8f9fa;
        border-radius: 8px;
        font-size: 13px;
    }

    .info-label {
        font-weight: 600;
        color: #667eea;
    }

    .candidate-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        justify-content: center;
    }

    .tag {
        padding: 4px 12px;
        background: #e8ecff;
        color: #667eea;
        border-radius: 15px;
        font-size: 11px;
        font-weight: 600;
    }

    .tag.available {
        background: #d1ecf1;
        color: #0c5460;
    }

    .tag.nl {
        background: #d4edda;
        color: #155724;
    }

    .tag.eu {
        background: #fff3cd;
        color: #856404;
    }

    .results-count {
        text-align: center;
        color: #667eea;
        font-size: 1.2em;
        font-weight: 600;
        margin-bottom: 30px;
    }
</style>
{% endblock %}

{% block content %}
<!-- Hero Banner -->
<section class="hero-banner">
    <div class="hero-content">
        <h1 class="text-5xl font-bold mb-6">{% trans "Znajdź Idealnego Kandydata" %}</h1>
        <p class="text-xl">{% trans "Anonimowa baza talentów oparta na umiejętnościach i doświadczeniu" %}</p>
    </div>
</section>

<!-- Search Section -->
<section class="search-section">
    <div class="search-card">
        <form method="get" action="{% url 'hrpartner:candidate_database' %}">
            <div class="search-input-wrapper">
                <input 
                    type="text" 
                    name="search"
                    class="search-input" 
                    value="{{ search_query }}"
                    placeholder="{% trans 'Szukaj według stanowiska, miasta, kraju, branży...' %}">
                <button type="submit" class="search-btn">{% trans "Szukaj" %}</button>
            </div>
        </form>
        
        <div class="quick-filters">
            <a href="?filter=all" class="quick-filter-btn {% if filter_type == 'all' or not filter_type %}active{% endif %}">
                {% trans "Wszyscy" %}
            </a>
            <a href="?filter=available" class="quick-filter-btn {% if filter_type == 'available' %}active{% endif %}">
                {% trans "Dostępni" %}
            </a>
            <a href="?filter=nl" class="quick-filter-btn {% if filter_type == 'nl' %}active{% endif %}">
                {% trans "Doświadczenie NL" %}
            </a>
            <a href="?filter=eu" class="quick-filter-btn {% if filter_type == 'eu' %}active{% endif %}">
                {% trans "Doświadczenie EU" %}
            </a>
            <a href="?filter=construction" class="quick-filter-btn {% if filter_type == 'construction' %}active{% endif %}">
                {% trans "Budownictwo" %}
            </a>
            <a href="?filter=production" class="quick-filter-btn {% if filter_type == 'production' %}active{% endif %}">
                {% trans "Produkcja" %}
            </a>
        </div>
    </div>
</section>

<!-- Results Count -->
<div class="results-count">
    {{ total_count }} {% trans "kandydatów" %}
</div>

<!-- Candidates Grid -->
<div class="candidates-grid">
    {% for candidate in candidates %}
    <div class="candidate-card" onclick="window.location.href='{% url 'hrpartner:candidate_detail' candidate.pk %}'">
        <div class="candidate-avatar">
            {% if candidate.photo %}
                <img src="{{ candidate.photo.url }}" alt="{{ candidate.code }}" style="width:100%; height:100%; border-radius:50%; object-fit:cover;">
            {% else %}
                {{ candidate.code|slice:"-2:" }}
            {% endif %}
        </div>
        
        <div class="candidate-code">{{ candidate.code }}</div>
        <div class="candidate-position">{{ candidate.position }}</div>
        
        <div class="candidate-info">
            {% if candidate.age %}
            <div class="info-row">
                <span class="info-label">{% trans "Wiek" %}</span>
                <span class="info-value">{{ candidate.age }}</span>
            </div>
            {% endif %}
            
            <div class="info-row">
                <span class="info-label">{% trans "Kraj" %}</span>
                <span class="info-value">{{ candidate.country }}</span>
            </div>
            
            {% if candidate.city %}
            <div class="info-row">
                <span class="info-label">{% trans "Miasto" %}</span>
                <span class="info-value">{{ candidate.city }}</span>
            </div>
            {% endif %}
            
            <div class="info-row">
                <span class="info-label">{% trans "Doświadczenie" %}</span>
                <span class="info-value">{{ candidate.experience_years }}y</span>
            </div>
        </div>
        
        <div class="candidate-tags">
            {% for tag in candidate.get_tags_list %}
                <span class="tag">{{ tag }}</span>
            {% endfor %}
            
            {% if candidate.available %}
                <span class="tag available">{% trans "Dostępny" %}</span>
            {% endif %}
            
            {% if candidate.worked_in_nl %}
                <span class="tag nl">NL</span>
            {% endif %}
            
            {% if candidate.worked_in_eu %}
                <span class="tag eu">EU</span>
            {% endif %}
        </div>
    </div>
    {% empty %}
    <div style="grid-column: 1/-1; text-align:center; padding:80px 20px; color:#666;">
        {% trans "Nie znaleziono kandydatów spełniających kryteria" %}
    </div>
    {% endfor %}
</div>
{% endblock %}
"""


# ==== 6. AKTUALIZACJA base.html (DODAJ DO NAWIGACJI) ====
"""
W sekcji <nav> dodaj link:
<a href="{% url 'hrpartner:candidate_database' %}" class="hover:text-blue-600">
    {% trans "Baza CV" %}
</a>
"""


# ==== 7. management/commands/populate_candidates.py (DANE TESTOWE) ====
"""
from django.core.management.base import BaseCommand
from hrpartner.models import Candidate

class Command(BaseCommand):
    help = 'Populate database with sample candidates'

    def handle(self, *args, **kwargs):
        candidates_data = [
            {
                'code': 'CAND-001',
                'position': 'Carpenter / Stolarz',
                'age': 32,
                'country': 'Poland',
                'city': 'Warsaw',
                'experience_years': 8,
                'industry': 'construction',
                'tags': 'Construction, Carpenter, Woodworking',
                'available': True,
                'worked_in_nl': True,
                'worked_in_eu': True,
                'languages_spoken': 'pl'
            },
            {
                'code': 'CAND-002',
                'position': 'Production Worker',
                'age': 28,
                'country': 'Poland',
                'city': 'Krakow',
                'experience_years': 5,
                'industry': 'production',
                'tags': 'Production, Assembly',
                'available': True,
                'worked_in_nl': False,
                'worked_in_eu': True,
                'languages_spoken': 'pl'
            },
            # Dodaj więcej według potrzeb...
        ]
        
        for data in candidates_data:
            Candidate.objects.get_or_create(
                code=data['code'],
                defaults=data
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated candidates'))


# Uruchom: python manage.py populate_candidates
"""


