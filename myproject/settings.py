from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# Bezpieczeństwo
# -----------------------
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-f1if(8j!4p9j9jx0=*3z38b^d78xcu8#2#19cvmw^o3^6!1pgx'
)
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get(
    'DJANGO_ALLOWED_HOSTS',
    'localhost,127.0.0.1,job.hrconsultingpartner.nl,www.job.hrconsultingpartner.nl'
).split(',')

# -----------------------
# Aplikacje
# -----------------------
INSTALLED_APPS = [
    'modeltranslation',
    'corsheaders',      # ⬅️ OK
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'candidates',
    'Ogloszeniafirm',
]

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # ⬅️ OK
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

# -----------------------
# Templates
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# -----------------------
# Bazy danych
# -----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'candidates.sqlite3',
    },
    'jobs_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'ogloszeniafirm.sqlite3',
    }
}

DATABASE_ROUTERS = ['myproject.dbrouters.JobsRouter']

# -----------------------
# Statyczne pliki
# -----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------
# CORS
# -----------------------
# myproject/settings.py

ALLOWED_HOSTS = [ 
    'localhost',
    '127.0.0.1',
    'app-1-sg16.onrender.com',  # ⬅️ DODAJ TO
    'job.hrconsultingpartner.nl',
    'www.job.hrconsultingpartner.nl',
]

# CORS - pozwól na requesty z Antagonist
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'https://job.hrconsultingpartner.nl',  # Antagonist
    'https://www.job.hrconsultingpartner.nl',
]


CORS_ALLOW_CREDENTIALS = True

# -----------------------
# Internacjonalizacja
# -----------------------
LANGUAGE_CODE = 'pl'

LANGUAGES = [
    ('pl', 'Polski'),
    ('en', 'English'),
    ('nl', 'Nederlands'),
    ('de', 'Deutsch'),
    ('bg', 'Български'),
    ('ru', 'Русский'),
    ('uk', 'Українська'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'pl'

LOCALE_PATHS = [BASE_DIR / 'locale']

TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'