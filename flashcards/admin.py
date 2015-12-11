from django.contrib import admin
from .models import User, Dictionary, Dictionary_Flashcard, Flashcard, Language

# Register your models here.
admin.site.register(User)
admin.site.register(Dictionary)
admin.site.register(Dictionary_Flashcard)
admin.site.register(Flashcard)
admin.site.register(Language)