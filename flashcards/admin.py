from django.contrib import admin
from .models import Dictionary, Dictionary_Flashcard, Flashcard, Language

admin.site.register(Dictionary)
admin.site.register(Dictionary_Flashcard)
admin.site.register(Flashcard)
admin.site.register(Language)