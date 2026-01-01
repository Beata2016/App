from django.shortcuts import render
from candidates.models import Candidate
from Ogloszeniafirm.models import JobPosting

# Strona główna
def index(request):
    latest_jobs = JobPosting.objects.filter(is_active=True).order_by('-posted_at')[:6]
    latest_candidates = Candidate.objects.all().order_by('-created_at')[:6]
    context = {'jobs': latest_jobs, 'candidates': latest_candidates}
    return render(request, 'index.html', context)

# Pozostałe Twoje widoki
def firma(request):
    return render(request, 'firma.html')

def overons(request):
    return render(request, 'Overons.html')

def contactus(request):
    return render(request, 'contactus2.html')

def ai_chat(request):
    return render(request, 'ai_chat.html')

def cv_base(request):
    candidates_list = Candidate.objects.all().order_by('-created_at')
    context = {'candidates': candidates_list}
    return render(request, 'listcccc.html', context)

def vacatures(request):
    jobs_list = JobPosting.objects.filter(is_active=True).order_by('-posted_at')
    context = {'jobs': jobs_list}
    return render(request, 'job_list.html', context)

def voor_bedrijven(request):
    return render(request, 'voor_bedrijven.html', {})

