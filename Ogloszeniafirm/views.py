# Ogloszeniafirm/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import JobPosting
import json

# ===========================
# GOOGLE GEMINI AI - DARMOWE
# ===========================
try:
    import google.generativeai as genai
    
    # ⚠️ WKLEJ TUTAJ SWÓJ API KEY Z: https://aistudio.google.com/apikey
    GEMINI_API_KEY = 'YOUR_API_KEY_HERE'  # ← ZAMIEŃ TO!
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    AI_ENABLED = True
except ImportError:
    AI_ENABLED = False
    print("⚠️ Google Generative AI nie zainstalowane. Uruchom: pip install google-generativeai")


# ===========================
# SŁOWNIKI TŁUMACZEŃ
# ===========================
TRANSLATIONS = {
    'en': {
        'page_title': 'Job Offers',
        'nav_home': 'Home',
        'nav_about': 'About',
        'nav_companies': 'For Companies',
        'nav_contact': 'Contact',
        'hero_title': 'Find Your Dream Job',
        'hero_subtitle': 'Thousands of job offers across Europe • Verified companies • Quick application',
        'search_placeholder': 'Position, company, location...',
        'btn_search': 'Search',
        'filters_title': 'Filters',
        'btn_clear': 'Clear',
        'filter_country': 'Country',
        'filter_location': 'City',
        'filter_role': 'Position',
        'filter_type': 'Contract type',
        'filter_language': 'Language',
        'all_countries': 'All countries',
        'all_cities': 'All cities',
        'all_roles': 'All positions',
        'all_types': 'All types',
        'all_languages': 'Any language',
        'found': 'Found',
        'offers': 'offers',
        'sort_newest': 'Newest',
        'sort_salary': 'Best paid',
        'accommodation': 'Accommodation',
        'transport': 'Transport',
        'week': 'week',
        'btn_apply': 'Apply now',
        'btn_save': 'Save',
        'no_results_title': 'No offers found',
        'no_results_text': 'Try changing your search criteria or clear filters',
    },
    'nl': {
        'page_title': 'Vacatures',
        'nav_home': 'Home',
        'nav_about': 'Over ons',
        'nav_companies': 'Voor bedrijven',
        'nav_contact': 'Contact',
        'hero_title': 'Vind je droombaan',
        'hero_subtitle': 'Duizenden vacatures in heel Europa • Geverifieerde bedrijven • Snelle sollicitatie',
        'search_placeholder': 'Functie, bedrijf, locatie...',
        'btn_search': 'Zoeken',
        'filters_title': 'Filters',
        'btn_clear': 'Wissen',
        'filter_country': 'Land',
        'filter_location': 'Stad',
        'filter_role': 'Functie',
        'filter_type': 'Contract type',
        'filter_language': 'Taal',
        'all_countries': 'Alle landen',
        'all_cities': 'Alle steden',
        'all_roles': 'Alle functies',
        'all_types': 'Alle types',
        'all_languages': 'Elke taal',
        'found': 'Gevonden',
        'offers': 'vacatures',
        'sort_newest': 'Nieuwste',
        'sort_salary': 'Beste betaald',
        'accommodation': 'Accommodatie',
        'transport': 'Transport',
        'week': 'week',
        'btn_apply': 'Solliciteer nu',
        'btn_save': 'Opslaan',
        'no_results_title': 'Geen vacatures gevonden',
        'no_results_text': 'Probeer je zoekcriteria te wijzigen of filters te wissen',
    },
    'pl': {
        'page_title': 'Oferty Pracy',
        'nav_home': 'Strona główna',
        'nav_about': 'O nas',
        'nav_companies': 'Dla firm',
        'nav_contact': 'Kontakt',
        'hero_title': 'Znajdź swoją wymarzoną pracę',
        'hero_subtitle': 'Tysiące ofert pracy w całej Europie • Sprawdzone firmy • Szybkie aplikowanie',
        'search_placeholder': 'Stanowisko, firma, lokalizacja...',
        'btn_search': 'Szukaj',
        'filters_title': 'Filtry',
        'btn_clear': 'Wyczyść',
        'filter_country': 'Kraj',
        'filter_location': 'Miasto',
        'filter_role': 'Stanowisko',
        'filter_type': 'Typ umowy',
        'filter_language': 'Język',
        'all_countries': 'Wszystkie kraje',
        'all_cities': 'Wszystkie miasta',
        'all_roles': 'Wszystkie stanowiska',
        'all_types': 'Wszystkie typy',
        'all_languages': 'Dowolny język',
        'found': 'Znaleziono',
        'offers': 'ofert',
        'sort_newest': 'Najnowsze',
        'sort_salary': 'Najlepiej płatne',
        'accommodation': 'Zakwaterowanie',
        'transport': 'Transport',
        'week': 'tydzień',
        'btn_apply': 'Aplikuj teraz',
        'btn_save': 'Zapisz',
        'no_results_title': 'Nie znaleziono ofert',
        'no_results_text': 'Spróbuj zmienić kryteria wyszukiwania lub wyczyść filtry',
    },
    # inne języki: 'cs', 'bg' (jak w oryginale)
}


# ===========================
# GŁÓWNA STRONA Z OFERTAMI + JĘZYKI
# ===========================
def job_list(request):
    """
    Wyświetla listę ofert pracy z inteligentnymi filtrami + obsługa języków.
    """
    current_lang = request.GET.get('lang', 'pl')
    if current_lang not in TRANSLATIONS:
        current_lang = 'pl'
    trans = TRANSLATIONS[current_lang]

    jobs = JobPosting.objects.filter(is_active=True)
    search_query = request.GET.get('q', '').strip()

    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(job_role__icontains=search_query) |
            Q(company_name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(country__icontains=search_query) |
            Q(industry__icontains=search_query) |
            Q(employment_type__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(requirements__icontains=search_query)
        )

    # Map GET parameters to model fields when names differ
    get_to_field = {
        'language': 'language_required',
        'remote': 'remote_option',
    }

    # Filtry szczegółowe (używaj dokładnego dopasowania dla pól wyboru)
    filters = ['job_role', 'industry', 'country', 'location', 'employment_type', 'language', 'weekly_hours', 'remote']
    for f in filters:
        val = request.GET.get(f, '').strip()
        if not val:
            continue

        field_name = get_to_field.get(f, f)
        # location powinno być partial match
        if f == 'location':
            jobs = jobs.filter(location__icontains=val)
        else:
            # bezpieczeństwo: tylko istniejące pola
            try:
                jobs = jobs.filter(**{field_name: val})
            except Exception:
                # ignoruj nieprawidłowe filtry zamiast podnosić wyjątek
                continue

    # Sortowanie
    sort = request.GET.get('sort', 'newest')
    if sort == 'salary':
        # sortuj po maksymalnym wynagrodzeniu, a potem po dacie
        jobs = jobs.order_by('-salary_max', '-salary_min', '-posted_at')
    else:
        jobs = jobs.order_by('-posted_at')

    # Paginacja — template oczekuje na `jobs.paginator.count`
    try:
        page = int(request.GET.get('page', 1))
    except (TypeError, ValueError):
        page = 1

    paginator = Paginator(jobs, 10)
    try:
        jobs_page = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        jobs_page = paginator.page(1)
    jobs = jobs_page

    # Opcje dropdown
    def choices_list(field_name):
        return [{'code': code, 'name': name} for code, name in JobPosting._meta.get_field(field_name).choices]

    context = {
        'jobs': jobs,
        'current_lang': current_lang,
        'trans': trans,
        'job_role_options': choices_list('job_role'),
        'industry_options': choices_list('industry'),
        'country_options': [{'code': code, 'name': name, 'flag': '🌍'} for code, name in JobPosting._meta.get_field('country').choices],
        'location_options': JobPosting.objects.filter(is_active=True).values_list('location', flat=True).distinct().order_by('location'),
        'employment_type_options': choices_list('employment_type'),
        'language_options': choices_list('language_required'),
        'current_search': search_query,
        'current_job_role': request.GET.get('job_role', ''),
        'current_industry': request.GET.get('industry', ''),
        'current_country': request.GET.get('country', ''),
        'current_location': request.GET.get('location', ''),
        'current_employment_type': request.GET.get('employment_type', ''),
        'current_language': request.GET.get('language', ''),
        'current_weekly_hours': request.GET.get('weekly_hours', ''),
        'current_remote': request.GET.get('remote', ''),
    }

    return render(request, 'ogloszeniafirm/job_list.html', context)


# ===========================
# AI CHAT - DARMOWY GEMINI
# ===========================
@csrf_exempt
def ai_chat(request):
    if not AI_ENABLED:
        return JsonResponse({'error': 'AI nie jest dostępne. Zainstaluj: pip install google-generativeai'}, status=500)
    if request.method != 'POST':
        return JsonResponse({'error': 'Tylko POST'}, status=400)

    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        if not user_message:
            return JsonResponse({'error': 'Pusta wiadomość'}, status=400)

        jobs = JobPosting.objects.filter(is_active=True)[:20]

        jobs_context = ""
        for idx, job in enumerate(jobs, 1):
            salary = job.get_salary_display_text()
            jobs_context += f"""
{idx}. {job.title} - {job.company_name}
   📍 {job.location}, {job.get_country_display()}
   💰 {salary}
   🏢 Branża: {job.get_industry_display()}
   ⏰ {job.get_employment_type_display()}
   🏠 Zakwaterowanie: {job.get_accommodation_display()}
   🚗 Transport: {job.get_transport_display()}
"""

        prompt = f"""Jesteś profesjonalnym asystentem HR specjalizującym się w rekrutacji międzynarodowej.
Pomagasz kandydatom znaleźć najlepsze oferty pracy.

DOSTĘPNE OFERTY PRACY:
{jobs_context}

PYTANIE UŻYTKOWNIKA:
{user_message}

INSTRUKCJE:
- Odpowiadaj TYLKO po angielsku
- Bądź pomocny, profesjonalny i konkretny
- Jeśli pytanie dotyczy konkretnej oferty - podaj jej szczegóły
- Jeśli użytkownik szuka pracy - zasugeruj 2-3 najlepsze oferty
- Jeśli pyta o wymagania/benefity - odpowiedz na podstawie danych
- Maksymalnie 4-5 zdań w odpowiedzi
- Użyj emoji dla czytelności: 📍 💰 🏢 ⏰ 🏠 🚗

ODPOWIEDZ:"""

        response = model.generate_content(prompt)
        return JsonResponse({'response': response.text})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Nieprawidłowy format JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Błąd AI: {str(e)}'}, status=500)


# ===========================
# API: Szczegóły oferty
# ===========================
def job_detail_api(request, job_id):
    """
    Zwraca szczegóły pojedynczej oferty w formacie JSON (dla AJAX).
    Obsługuje brak danych w polach opcjonalnych.
    """
    try:
        job = JobPosting.objects.get(id=job_id, is_active=True)

        def safe_get(attr, default="Brak danych"):
            value = getattr(job, attr, None)
            return value if value else default

        data = {
            'id': job.id,
            'title': job.title,
            'company': safe_get('company_name'),
            'location': safe_get('location'),
            'country': job.get_country_display(),
            'salary': job.get_salary_display_text(),
            'description': safe_get('description', "Brak opisu"),
            'requirements': safe_get('requirements', "Brak szczegółów"),
            'responsibilities': safe_get('responsibilities', "Brak szczegółów"),
            'benefits': safe_get('benefits', "Brak szczegółów"),
            'employment_type': job.get_employment_type_display(),
            'weekly_hours': job.get_weekly_hours_display() if job.weekly_hours else "Nie podano",
            'accommodation': job.get_accommodation_display(),
            'transport': job.get_transport_display(),
            'language': f"{job.get_language_required_display()} ({job.get_language_level_display()})"
                        if job.language_required else "Nie podano",
            'remote_option': job.get_remote_option_display() if hasattr(job, 'remote_option') else "Nie dotyczy",
            'posted_at': job.posted_at.strftime("%Y-%m-%d %H:%M") if job.posted_at else "Nieznana data",
        }

        return JsonResponse(data)

    except JobPosting.DoesNotExist:
        return JsonResponse({'error': 'Oferta nie istnieje'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Wystąpił błąd: {str(e)}'}, status=500)


def jobs_api(request):
    """
    Zwraca listę ostatnich aktywnych ogłoszeń w formacie JSON.
    Przydatne dla statycznego frontendu (fetch).
    """
    try:
        limit = int(request.GET.get('limit', 20))
    except ValueError:
        limit = 20

    jobs_qs = JobPosting.objects.filter(is_active=True).order_by('-posted_at')[:limit]
    jobs = []
    for job in jobs_qs:
        jobs.append({
            'id': job.id,
            'title': job.title,
            'company': job.company_name,
            'location': job.location,
            'country': job.get_country_display(),
            'language': job.get_language_required_display() if job.language_required else '',
            'posted_at': job.posted_at.strftime('%Y-%m-%d') if job.posted_at else '',
            'salary': job.get_salary_display_text(),
        })

    return JsonResponse({'results': jobs})
