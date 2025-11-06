from modeltranslation.translator import translator, TranslationOptions
from .models import JobPosting

class JobPostingTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'requirements',
        'responsibilities',
        'benefits',
        'additional_info',
        'location',
        'company_name',
    )

translator.register(JobPosting, JobPostingTranslationOptions)
