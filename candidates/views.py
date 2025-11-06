from django.shortcuts import render
from .models import Candidate


def candidates_list(request):
    candidates = Candidate.objects.all()

    # --- Filtry ---
    country = request.GET.get('country')
    if country:
        candidates = candidates.filter(country__icontains=country)

    city = request.GET.get('city')
    if city:
        candidates = candidates.filter(city__icontains=city)

    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    if min_age:
        candidates = candidates.filter(age__gte=min_age)
    if max_age:
        candidates = candidates.filter(age__lte=max_age)

    max_experience = request.GET.get('max_experience')
    if max_experience:
        candidates = candidates.filter(years_experience__lte=max_experience)

    language = request.GET.get('language')
    if language:
        candidates = candidates.filter(languages__language__icontains=language)

    industry = request.GET.get('industry')
    if industry:
        candidates = candidates.filter(industry__icontains=industry)

    position = request.GET.get('position')
    if position:
        candidates = candidates.filter(desired_position__icontains=position)

    # Checkboxy
    netherlands = request.GET.get('netherlands')
    if netherlands:
        candidates = candidates.filter(worked_in_nl=True)

    eu = request.GET.get('eu')
    if eu:
        candidates = candidates.filter(worked_in_eu=True)

    available = request.GET.get('available')
    if available:
        candidates = candidates.filter(available_for_contact=True)

    # --- Sortowanie ---
    candidates = candidates.order_by('-years_experience', 'age')

    return render(request, 'candidates/list.html', {'candidates': candidates})


