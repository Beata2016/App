# Deploy na Antagonist — krok po kroku

Ten dokument zawiera minimalne kroki, żeby wdrożyć pełne Django (zalecane) na hostingu Antagonist. Zakładam, że masz dostęp do panelu hostingu (file manager) i/lub SFTP oraz możliwość ustawiania zmiennych środowiskowych.

## Przed rozpoczęciem
- Upewnij się, że masz repozytorium z kodem projektu skopiowane na serwer albo że możesz przesłać pliki przez SFTP/FTP.
- Uzupełnij `requirements.txt` (w repo już jest podstawowa lista).
- Przygotuj wartości środowiskowe: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` (False w produkcji), `DJANGO_ALLOWED_HOSTS` (np. `job.hrconsultingpartner.nl,www.job.hrconsultingpartner.nl`).

## 1) Instalacja zależności (na serwerze)
Jeśli masz dostęp SSH (najczęściej Linux):

```bash
# w katalogu projektu
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

W PowerShell (Windows / lokalnie przed przesłaniem):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```


## 2) Ustaw zmienne środowiskowe
W panelu Antagonist ustaw:
- `DJANGO_SECRET_KEY` = (silny, losowy sekret)
- `DJANGO_DEBUG` = False
- `DJANGO_ALLOWED_HOSTS` = job.hrconsultingpartner.nl,www.job.hrconsultingpartner.nl

Jeśli nie możesz ustawić ich w panelu, dodaj je do pliku `.env` i załaduj w `settings.py` (albo użyj `export` w shellu przed uruchomieniem).

## 3) Migracje
Uruchom migracje dla obu baz:

```bash
python manage.py migrate
python manage.py migrate --database=jobs_db
```

## 4) Zbierz statyczne pliki

```bash
python manage.py collectstatic --noinput
```

To zapisze pliki w katalogu `STATIC_ROOT` (w `settings.py` ustawione na `staticfiles`). Upewnij się, że serwer potrafi serwować ten katalog — w Antagonist możesz wskazać katalog statyczny albo użyć WhiteNoise.

## 5) Konfiguracja WSGI/Passenger
Antagonist zwykle obsługuje aplikacje WSGI/Passenger. W panelu ustaw katalog aplikacji (gdzie jest `manage.py`) i wskaz entrypoint WSGI (`myproject.wsgi:application`). Po wdrożeniu zrestartuj aplikację przez panel.

Jeśli używasz Gunicorn (alternatywnie):
```bash
# przykład uruchomienia (w tle użyj systemd lub supervisor)
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```

## 6) Restart aplikacji
Po wykonaniu powyższych kroków zrestartuj usługę/Passenger z panelu Antagonist.

## 7) Sprawdzenia
- Otwórz stronę `https://job.hrconsultingpartner.nl/` i sprawdź, czy:
  - Strona główna ładuje się bez błędów.
  - Tło `/static/image/Foto12.jpg` jest dostępne.
  - Ogłoszenia wyświetlają się (jeśli w `jobs_db` są aktywne wpisy).
- Jeśli coś nie działa, sprawdź logi aplikacji (panel Antagonist ma logi błędów) oraz czy `STATIC_ROOT` jest poprawnie serwowany.

## Szybkie kroki FTP (jeśli nie masz SSH)
1. Wgraj cały katalog projektu (lub przynajmniej `templates/`, `static/`, `myproject/`, `manage.py`) przez FTP do katalogu aplikacji w panelu.
2. Upewnij się, że pliki zależności są zainstalowane — bez SSH musisz zainstalować zależności lokalnie i wgrać także katalog `venv` (niezalecane), lub poprosić support Antagonist o instalację.
3. Z poziomu panelu ustaw entrypoint WSGI i zrestartuj aplikację.

---

Jeśli chcesz, przygotuję też automatyczny skrypt PowerShell/Bash do uruchamiania wszystkich komend (pip install, migrate, collectstatic). Powiedz która metoda (SSH/Git/FTP) jest preferowana, to dopracuję instrukcję i skrypty.
