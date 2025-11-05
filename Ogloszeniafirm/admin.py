from django.contrib import admin
from .models import JobPosting

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    """
    Konfiguracja panelu administracyjnego dla ofert pracy
    """
    
    # Pola wyświetlane na liście ofert
    list_display = [
        'title', 
        'company_name', 
        'job_role', 
        'country',
        'location', 
        'remote_option',
        'employment_type',
        'is_active', 
        'posted_at'
    ]
    
    # Pola, po których można filtrować
    list_filter = [
        'is_active',
        'country',
        'remote_option',
        'industry',
        'employment_type',
        'language_required',
        'posted_at'
    ]
    
    # Pole wyszukiwania
    search_fields = [
        'title',
        'company_name',
        'location',
        'description'
    ]
    
    # Możliwość edycji bezpośrednio na liście
    list_editable = ['is_active']
    
    # Domyślne sortowanie (najnowsze na górze)
    ordering = ['-posted_at']
    
    # Ile ofert na stronie
    list_per_page = 25
    
    # Organizacja pól w formularzu edycji
    fieldsets = (
        ('Podstawowe informacje / Basic Information', {
            'fields': (
                'title',
                'company_name',
                'industry',
                'job_role',
                'description'
            )
        }),
        ('Lokalizacja / Location', {
            'fields': (
                'country',
                'location',
                'remote_option'
            )
        }),
        ('Wymagania językowe / Language Requirements', {
            'fields': (
                'language_required',
                'language_level'
            )
        }),
        ('Warunki zatrudnienia / Employment Conditions', {
            'fields': (
                'employment_type',
                'weekly_hours',
                'overtime'
            )
        }),
        ('Dodatkowe informacje / Additional Information', {
            'fields': (
                'additional_info',
                'is_active'
            ),
            'classes': ('collapse',)  # Sekcja zwinięta domyślnie
        }),
    )
    
    # Pola tylko do odczytu
    readonly_fields = ['posted_at']
    
    # Akcje masowe
    actions = ['activate_jobs', 'deactivate_jobs']
    
    def activate_jobs(self, request, queryset):
        """Aktywuj zaznaczone oferty"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} ofert(y) zostało aktywowanych.')
    activate_jobs.short_description = "Aktywuj zaznaczone oferty"
    
    def deactivate_jobs(self, request, queryset):
        """Dezaktywuj zaznaczone oferty"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} ofert(y) zostało dezaktywowanych.')
    deactivate_jobs.short_description = "Dezaktywuj zaznaczone oferty"