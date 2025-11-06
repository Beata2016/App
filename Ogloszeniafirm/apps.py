from django.apps import AppConfig

class OgloszeniafirmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ogloszeniafirm'

    def ready(self):
        import Ogloszeniafirm.translation  # ⬅️ załaduj tłumaczenia modeli


