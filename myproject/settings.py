from pathlib import Path
import os

# -----------------------
# Ścieżki bazowe
# -----------------------
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
    'localhost,127.0.0.1'
).split(',')

# -----------------------
# Aplikacje
# -----------------------
INSTALLED_APPS = [
    'modeltranslation',
    'corsheaders',
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
    'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [BASE_DIR / 'templates'],
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
IS_PRODUCTION = os.environ.get('PRODUCTION', 'False') == 'True'

if IS_PRODUCTION:
    # Produkcja - MySQL na serwerze Antagonist
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DB_CANDIDATES', 'deb98572_django'),
            'USER': os.environ.get('MYSQL_USER', 'deb98572_django'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'Rudie2025!'),
            'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
            'PORT': os.environ.get('MYSQL_PORT', '3306'),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
            },
        },
        'jobs_db': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DB_JOBS', 'deb98572_jobs'),
            'USER': os.environ.get('MYSQL_USER_JOBS', 'deb98572_jobs'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD_JOBS', 'Rudie2025!'),
            'HOST': os.environ.get('MYSQL_HOST_JOBS', 'localhost'),
            'PORT': os.environ.get('MYSQL_PORT_JOBS', '3306'),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
            },
        }
    }
    DATABASE_ROUTERS = ['myproject.dbrouters.JobsRouter']
else:
    # Lokalne - SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
        'jobs_db': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db_jobs.sqlite3',
        }
    }
    DATABASE_ROUTERS = ['myproject.dbrouters.JobsRouter']

# -----------------------
# Walidacja haseł
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------
# Statyczne pliki
# -----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------
# Pliki media
# -----------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------
# CORS
# -----------------------
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
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

