from .models import Todo, Type
from modeltranslation.translator import TranslationOptions,register

@register(Type)
class TypeTranslationOptions(TranslationOptions):
    fields = ('status',)

@register(Todo)
class TodoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
