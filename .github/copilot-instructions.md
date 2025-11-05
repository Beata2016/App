## Quick orientation — HR prototype (Django)

This repo is a small Django site (generated with Django 5.x). Key facts an AI coding agent must know to be productive immediately:

- Project root: `myproject/` (Django settings, URL routing, WSGI/ASGI).
- Apps of interest:
  - `candidates` — candidate profiles (default database)
  - `Ogloszeniafirm` — job postings (routed to a separate DB)
- Templates: shared templates folder at `templates/` plus app templates under each app's `templates/`.
- Static assets live in `static/` and are served from `STATICFILES_DIRS` in `myproject/settings.py`.

## Important structural decisions

- Two separate SQLite databases are used. See `myproject/settings.py` and `myproject/dbrouters.py`:
  - `default` -> `candidates.sqlite3` (models in `candidates` app)
  - `jobs_db` -> `ogloszeniafirm.sqlite3` (models in `Ogloszeniafirm` app)
- DB router: `myproject.dbrouters.JobsRouter` routes all reads/writes and migrations for app label `Ogloszeniafirm` to `jobs_db`. When changing job-posting models or migrations, ensure operations target `jobs_db`.

## Developer workflows & commands (repo-specific)

- Run dev server (standard Django):
  - `python manage.py runserver`
- Migrations (note multi-db):
  - Apply `candidates` (default DB): `python manage.py migrate`
  - Apply `Ogloszeniafirm` to jobs DB explicitly: `python manage.py migrate --database=jobs_db`
  - When creating migrations: `python manage.py makemigrations candidates` or `... Ogloszeniafirm` as appropriate.
- Shell queries: examples in code — e.g. `JobPosting.objects.filter(is_active=True).order_by('-posted_at')[:6]` (see `myproject/views.py`).

## Patterns & conventions seen in the codebase

- Multi-language labels: many `CHOICES` in models contain bilingual/multilingual strings (Polish / English). Keep choices immutable unless you also update related templates and migrations.
- Candidate unique code: `Candidate.save()` builds `candidate_code` by aggregating max(id) (see `candidates/models.py`); be careful with concurrency and tests that create many objects — tests may need explicit sequence control.
- App URL wiring: `myproject/urls.py` mounts apps:
  - `path('ogloszenia/', include('Ogloszeniafirm.urls'))`
  - `path('baza-danych/', include('candidates.urls'))`
  - root index view at `myproject.views.index`

## Files to inspect for any change related to feature or bug

- `myproject/settings.py` — DB names, INSTALLED_APPS, template dirs, staticfiles
- `myproject/dbrouters.py` — DB routing rules (important for migrations & queries)
- `myproject/urls.py` and `myproject/views.py` — site entry points and examples of model usage
- `candidates/models.py`, `Ogloszeniafirm/models.py` — domain models and CHOICES
- `candidates/urls.py`, `Ogloszeniafirm/urls.py` — app endpoints

## When editing models or migrations

- If you modify models in `Ogloszeniafirm`, run `makemigrations` and `migrate --database=jobs_db` — migrations for that app must be applied to `jobs_db`.
- Do not assume a single `migrate` will affect both DB files; the router's `allow_migrate` enforces separation.

## Known gaps / things to ask the human maintainer

- `requirements.txt` in the repository root is empty — confirm the target Python dependencies (Django version is stated in `settings.py` header: 5.2.7) and whether a virtualenv is checked in.
- Confirm whether the checked-in SQLite DB files are intended to be authoritative fixtures or local developer databases.

## Example edits an agent can safely make

- Small template changes in `templates/` or `templates/candidates/` that don't alter model contracts.
- Add form validation or small view logic that uses existing model fields (follow the CHOICES naming and international labels).

If anything here is unclear or you want more detail (example: preferred test runner, CI configuration, or dependency pinning), tell me which area to expand and I will update this file.
