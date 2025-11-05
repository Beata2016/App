import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
try:
    import django
    django.setup()
except Exception as e:
    print('Django setup failed:', e)
    sys.exit(1)

try:
    from Ogloszeniafirm.models import JobPosting
except Exception as e:
    print('Importing JobPosting failed:', e)
    sys.exit(1)

try:
    active_count = JobPosting.objects.filter(is_active=True).count()
    total_count = JobPosting.objects.count()
    print(f'JobPosting: total={total_count}, active={active_count}')

    qs = JobPosting.objects.order_by('-posted_at')[:5]
    print('Latest jobs (up to 5):')
    for j in qs:
        try:
            posted = j.posted_at.isoformat() if getattr(j, 'posted_at', None) else 'N/A'
        except Exception:
            posted = str(getattr(j, 'posted_at', 'N/A'))
        print(f'  id={j.id} title={getattr(j,"title","(no title)")} company={getattr(j,"company","(no company)")} posted_at={posted}')
except Exception as e:
    print('Query failed:', e)
    sys.exit(1)
