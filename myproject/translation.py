# Ogloszeniafirm/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import JobPosting

@register(JobPosting)
class JobPostingTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
