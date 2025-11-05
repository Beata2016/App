from django.apps import AppConfig  # <- TO JEST KONIECZNE

class CandidatesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidates'  # musi pasować do folderu aplikacji
    verbose_name = 'Candidate Management'


