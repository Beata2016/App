import sys
import os
from pathlib import Path

# katalog główny projektu (tam, gdzie jest manage.py)
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# ustawienia Django – podaj prawidłowy katalog settings dla projektu kandydatów
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "candidates.settings")  # jeśli settings.py jest w katalogu candidates

# uruchomienie aplikacji Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
