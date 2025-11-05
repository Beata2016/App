# myproject/views.py
from django.shortcuts import render
from candidates.models import Candidate
from Ogloszeniafirm.models import JobPosting

def index(request):
    """
    Widok strony głównej - wyświetla najnowsze ogłoszenia i CV
    """
    # Pobierz 6 najnowszych aktywnych ogłoszeń
    latest_jobs = JobPosting.objects.filter(is_active=True).order_by('-posted_at')[:6]
    
    # Pobierz 6 najnowszych kandydatów
    latest_candidates = Candidate.objects.all().order_by('-created_at')[:6]
    
    context = {
        'jobs': latest_jobs,
        'candidates': latest_candidates,
    }
    
    return render(request, 'index.html', context)