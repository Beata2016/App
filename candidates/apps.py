from django.apps import AppConfig

class CandidatesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidates'

    def ready(self):
        import candidates.translation  # ⬅️ wczytuje tłumaczenia modeli przy starcie

