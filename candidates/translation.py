from modeltranslation.translator import translator, TranslationOptions
from .models import Candidate

class CandidateTranslationOptions(TranslationOptions):
    # używamy pola 'bio' zamiast nieistniejącego 'about'
    fields = ('bio',)

translator.register(Candidate, CandidateTranslationOptions)


