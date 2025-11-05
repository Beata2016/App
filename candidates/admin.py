from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'candidate_code',
        'desired_position',
        'city',
        'country',
        'years_experience',
        'available_for_contact',
        'worked_in_eu',
        'worked_in_nl',
    )
    readonly_fields = ('candidate_code',)  # Kod generowany automatycznie
