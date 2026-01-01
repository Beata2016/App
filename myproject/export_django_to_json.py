"""
Skrypt do eksportu danych z Django do plików JSON z obsługą pełnej wielojęzyczności
Uruchom: python export_django_to_json.py
"""
import os
import json
from datetime import datetime, date
import django
# import modeli
from candidates.models import Candidate
from Ogloszeniafirm.models import OfertaPracy  # ⬅️ ZAKOMENTUJ TO

# ustawienie settings Twojego projektu
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hr_prototype.settings')
django.setup()

# import modeli
from candidates.models import Candidate
from Ogloszeniafirm.models import JobPosting

# test: wyświetlenie wszystkich obiektów
print("Kandydaci:", Candidate.objects.count())
print("Oferty:", OfertaPracy.objects.count())

# --- Funkcja pomocnicza do serializacji dat ---
def serialize_date(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%d')
    return str(obj) if obj else ''

# --- Tłumaczenia ---
GENDER_TRANSLATIONS = {
    'M': {'pl': 'Mężczyzna', 'nl': 'Man', 'en': 'Male'},
    'F': {'pl': 'Kobieta', 'nl': 'Vrouw', 'en': 'Female'},
    'O': {'pl': 'Inna', 'nl': 'Andere', 'en': 'Other'},
}

INDUSTRY_TRANSLATIONS = {
    'CONSTRUCTION': {'pl': 'Budownictwo', 'nl': 'Bouw', 'en': 'Construction'},
    'IT': {'pl': 'IT i teleinformatyka', 'nl': 'IT', 'en': 'IT & Telecommunications'},
    'PRODUCTION': {'pl': 'Produkcja', 'nl': 'Productie', 'en': 'Production'},
    'LOGISTICS': {'pl': 'Logistyka', 'nl': 'Logistiek', 'en': 'Logistics'},
    'AGRICULTURE': {'pl': 'Rolnictwo', 'nl': 'Landbouw', 'en': 'Agriculture'},
    'OTHER': {'pl': 'Inne', 'nl': 'Andere', 'en': 'Other'},
}

JOB_ROLE_TRANSLATIONS = {
    'CARPENTER': {'pl': 'Stolarz', 'nl': 'Timmerman', 'en': 'Carpenter'},
    'MASON': {'pl': 'Murarz', 'nl': 'Metselaar', 'en': 'Mason'},
    'ELECTRICIAN': {'pl': 'Elektryk', 'nl': 'Elektricien', 'en': 'Electrician'},
    'PLUMBER': {'pl': 'Hydraulik', 'nl': 'Loodgieter', 'en': 'Plumber'},
    'WELDER': {'pl': 'Spawacz', 'nl': 'Lasser', 'en': 'Welder'},
    'DRIVER': {'pl': 'Kierowca', 'nl': 'Chauffeur', 'en': 'Driver'},
    'TECHNICIAN': {'pl': 'Technik', 'nl': 'Technicus', 'en': 'Technician'},
    'OTHER': {'pl': 'Inne', 'nl': 'Andere', 'en': 'Other'},
}

ACCOMMODATION_TRANSLATIONS = {
    'HAS': {'pl': 'Posiada', 'nl': 'Heeft', 'en': 'Has accommodation'},
    'NONE': {'pl': 'Brak', 'nl': 'Geen', 'en': 'None'},
    'OTHER': {'pl': 'Inne', 'nl': 'Andere', 'en': 'Other'},
}

# --- Funkcja eksportu kandydatów ---
def export_kandydaci():
    kandydaci = Candidate.objects.all()
    dane = []

    for k in kandydaci:
        gender = k.gender or ''
        industry = k.industry or ''
        job_role = k.job_role or ''
        accommodation = k.accommodation_nl or ''

        kandydat_dict = {
            'id': k.id,
            'candidate_code': k.candidate_code,
            'imie': '',  # Brak w modelu - pusty
            'nazwisko': '',  # Brak w modelu - pusty
            'gender': gender,
            'gender_translations': GENDER_TRANSLATIONS.get(gender, {}),
            'age': k.age or 0,
            'job_role': job_role,
            'job_role_translations': JOB_ROLE_TRANSLATIONS.get(job_role, {}),
            'wyksztalcenie': '',  # Brak w modelu
            'doswiadczenie': f"{k.years_experience} lat" if k.years_experience else '',
            'lokalizacja': k.city or '',
            'city': k.city or '',
            'country': k.country or 'pl',
            'industry': industry,
            'industry_translations': INDUSTRY_TRANSLATIONS.get(industry, {}),
            'desired_position': k.desired_position or '',
            'years_experience': k.years_experience or 0,
            'bio': k.bio or '',
            'avatar_url': k.avatar_url or '',
            'available_for_contact': k.available_for_contact,
            'worked_in_eu': k.worked_in_eu,
            'worked_in_nl': k.worked_in_nl,
            'accommodation_nl': accommodation,
            'accommodation_translations': ACCOMMODATION_TRANSLATIONS.get(accommodation, {}),
            'data_dodania': serialize_date(k.created_at),
        }
        dane.append(kandydat_dict)

    with open('kandydaci.json', 'w', encoding='utf-8') as f:
        json.dump(dane, f, ensure_ascii=False, indent=2)
    print(f"✓ Wyeksportowano {len(dane)} kandydatów do kandydaci.json")
    return len(dane)

# --- Funkcja eksportu ofert pracy ---
def export_oferty():
    oferty = JobPosting.objects.all()
    dane = []

    for o in oferty:
        oferta_dict = {
            'id': o.id,
            'tytul': getattr(o, 'title', '') or getattr(o, 'tytul', ''),
            'firma': getattr(o, 'company_name', '') or getattr(o, 'firma', ''),
            'lokalizacja': getattr(o, 'location', '') or getattr(o, 'lokalizacja', ''),
            'opis': getattr(o, 'description', '') or getattr(o, 'opis', ''),
            'wynagrodzenie': getattr(o, 'salary', '') or getattr(o, 'wynagrodzenie', ''),
            'typ_zatrudnienia': getattr(o, 'employment_type', ''),
            'aktywna': getattr(o, 'is_active', True),
            'data_dodania': serialize_date(getattr(o, 'created_at', None) or getattr(o, 'posted_at', None)),
        }
        dane.append(oferta_dict)

    with open('oferty.json', 'w', encoding='utf-8') as f:
        json.dump(dane, f, ensure_ascii=False, indent=2)
    print(f"✓ Wyeksportowano {len(dane)} ofert do oferty.json")
    return len(dane)

# --- Uruchomienie skryptu ---
if __name__ == '__main__':
    print("=" * 60)
    print("EKSPORT DANYCH Z DJANGO DO JSON")
    print("=" * 60)
    try:
        count_kandydaci = export_kandydaci()
        count_oferty = export_oferty()
        print("=" * 60)
        print(f"✓ Eksport zakończony pomyślnie!")
        print(f"  - Kandydaci: {count_kandydaci}")
        print(f"  - Oferty: {count_oferty}")
        print("=" * 60)
    except Exception as e:
        print("=" * 60)
        print(f"✗ Błąd podczas eksportu: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()