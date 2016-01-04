from django.contrib import admin
from .models import Dictionary, Flashcards_Dictionary, Flashcard, Language

admin.site.register(Dictionary)
admin.site.register(Flashcards_Dictionary)
admin.site.register(Flashcard)
admin.site.register(Language)