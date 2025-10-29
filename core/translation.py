# translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import SiteInfo

@register(SiteInfo)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('address', 'about_text', 'work_hour1', 'work_hour2', 'work_hour3')
