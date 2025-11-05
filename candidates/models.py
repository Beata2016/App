from django.db import models

# ===========================
# Choices / Listy wyboru
# ===========================

INDUSTRY_CHOICES = [
    ('PRODUCTION', 'Production / Produkcja'),
    ('AGRICULTURE', 'Agriculture / Rolnictwo'),
    ('CLEANING', 'Cleaning / Sprzątanie'),
    ('CONSTRUCTION', 'Construction / Budownictwo'),
    ('LOGISTICS', 'Logistics / Transport'),
    ('DRIVERS', 'Drivers / Kierowcy'),
    ('HEALTHCARE', 'Healthcare / Opieka'),
    ('FINANCE', 'Finance / Finanse'),
    ('ADMINISTRATION', 'Administration / Administracja'),
    ('TECHNICAL', 'Technical / Techniczne'),
    ('IT', 'IT / Informatyka'),
    ('HORECA', 'Horeca / Gastronomia'),
    ('ENERGY', 'Energy / Energetyka'),
    ('MARKETING', 'Marketing / PR'),
    ('SALES', 'Sales / Sprzedaż'),
    ('HR', 'HR / Szkolenia'),
    ('RND', 'R&D / Badania'),
    ('OTHER', 'Other / Inne'),
]

JOB_ROLE_CHOICES = [
    ('CARPENTER', 'Carpenter / Timmerman / Stolarz / Tischler / Truhlář / Дърводелец / Столяр / Деревороб'),
    ('MASON', 'Mason / Metselaar / Murarz / Maurer / Zedník / Каменоделец / Каменар / Каменяр'),
    ('CONSTRUCTION_HELPER', 'Construction Helper / Bouwhelper / Pomocnik budowlany / Bauhelfer / Строителен помощник / Будівельний помічник'),
    ('PAINTER', 'Painter / Schilder / Malarz / Maler / Malíř / Бояджия / Маляр'),
    ('PLASTERER', 'Plasterer / Stukadoor / Tynkarz / Stuckateur / Štuk / Тенекеджия / Штукатур'),
    ('PLUMBER', 'Plumber / Loodgieter / Hydraulik / Klempner / Instalatér / Водопроводчик / Водопровідник'),
    ('ELECTRICIAN', 'Electrician / Elektricien / Elektryk / Elektriker / Elektrikář / Ел. техник / Електрик'),
    ('WELDER', 'Welder / Lasser / Spawacz / Schweißer / Svářeč / Зварник / Зварювальник'),
    ('WINDOW_INSTALLER', 'Window Installer / Raammonteur / Monter okien / Fensterbauer / Montér oken / Монтажник на прозорци / Монтажник вікон'),
    ('FAÇADE_INSTALLER', 'Facade Installer / Gevelmonteur / Monter fasad / Fassadenmonteur / Montér fasád / Монтажник на фасади / Монтажник фасадів'),
    ('TECHNICIAN', 'Technician / Technicus / Technik / Techniker / Техник / Технік'),
    ('PRODUCTION_WORKER', 'Production Worker / Productiemedewerker / Pracownik produkcji / Produktionsmitarbeiter / Výrobní pracovník / Працівник виробництва'),
    ('PHYSICAL_WORKER', 'Physical Worker / Fysiek werker / Pracownik fizyczny / Hilfsarbeiter / Фізичний працівник'),
    ('OPERATOR', 'Machine Operator / Operator maszyn / Obsluha strojů / Машинен оператор'),
    ('DRIVER', 'Driver / Chauffeur / Kierowca / Fahrer / Шофьор / Водій'),
    ('CLEANER', 'Cleaner / Schoonmaker / Pracownik sprzątający / Reiniger / Uklízeč / Прибиральник'),
    ('BUILDER', 'Construction Worker / Bouwer / Budowniczy / Bauarbeiter / Строител / Будівельник'),
    ('MECHANIC', 'Mechanic / Monteur / Mechanik / Mechaniker / Механік'),
    ('NURSE', 'Nurse / Verpleegkundige / Pielęgniarka / Krankenschwester / Zdravotní sestra / Медсестра'),
    ('ACCOUNTANT', 'Accountant / Boekhouder / Księgowy / Buchhalter / Счетоводител / Бухгалтер'),
    ('CHEF', 'Chef / Kok / Kucharz / Küchenchef / Šéfkuchař / Готвач / Шеф-кухар'),
    ('IT_SPECIALIST', 'IT Specialist / IT-specialist / Specjalista IT / IT-Spezialist / IT спеціаліст'),
    ('OTHER', 'Other / Overig / Inny / Други / Інше'),
]

LANGUAGE_CHOICES = [
    ('EN', 'English'),
    ('DE', 'German / Deutsch'),
    ('NL', 'Dutch / Nederlands'),
    ('PL', 'Polish / Polski'),
    ('RU', 'Russian / Русский'),
    ('CS', 'Czech / Česky'),
    ('BG', 'Bulgarian / Български'),
    ('UA', 'Ukrainian / Українська'),
]

LANGUAGE_LEVEL_CHOICES = [
    ('BASIC', 'Basic / Podstawowy'),
    ('INTERMEDIATE', 'Intermediate / Średni'),
    ('ADVANCED', 'Advanced / Zaawansowany'),
]

# ===========================
# Candidate Model
# ===========================
class Candidate(models.Model):
    
    candidate_code = models.CharField(max_length=20, unique=True, editable=False)
    age = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, blank=True, null=True)
    job_role = models.CharField(max_length=50, choices=JOB_ROLE_CHOICES, blank=True, null=True)
    desired_position = models.CharField(max_length=100, blank=True, null=True)
    years_experience = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True)
    available_for_contact = models.BooleanField(default=False)
    worked_in_eu = models.BooleanField(default=False)
    worked_in_nl = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.candidate_code:
            # Poprawka: używamy 'id' zamiast nieistniejącego 'id_nummer_kandidaat'
            last_id = Candidate.objects.aggregate(models.Max('id'))['id__max'] or 0
            self.candidate_code = f"Cand-{last_id + 1:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.candidate_code} ({self.job_role})"


# ===========================
# Job Experience
# ===========================
class JobExperience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='job_experiences')
    years_in_profession = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, choices=[
        ('PL', 'Poland / Polska'),
        ('NL', 'Netherlands / Holandia'),
        ('EU', 'Other EU / Inna UE')
    ])
    position_description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.candidate} - {self.country} ({self.years_in_profession} yrs)"


# ===========================
# Diploma
# ===========================
class Diploma(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='diplomas')
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, blank=True, null=True)
    year_obtained = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, choices=[
        ('PL', 'Poland / Polska'),
        ('NL', 'Netherlands / Holandia'),
        ('EU', 'Other EU / Inna UE')
    ])
    is_vca = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.candidate} - {self.name} ({self.country})"


# ===========================
# Candidate Languages
# ===========================
class CandidateLanguage(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='languages')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    level = models.CharField(max_length=20, choices=LANGUAGE_LEVEL_CHOICES)

    def __str__(self):
        return f"{self.candidate} - {self.language} ({self.level})"
