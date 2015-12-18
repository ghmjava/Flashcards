from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Language(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    description  = models.CharField(max_length=200)
    
    def __str__(self):
        return self.code

class Flashcard(models.Model):
    word = models.CharField(max_length=30)
    translation = models.CharField(max_length=30)
    language = models.ForeignKey(Language, related_name='language')
    translation_language = models.ForeignKey(Language, related_name='translation_language')
    owner = models.ForeignKey(User)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.word

class Dictionary(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    owner  = models.ForeignKey(User, related_name='dictionaries')
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dictionaries'

class Dictionary_Flashcard(models.Model):
    dictionary = models.ForeignKey(Dictionary, related_name='flashcards')
    flashcard = models.ForeignKey(Flashcard, related_name='dictionaries')
    hits = models.IntegerField(default=0)
    successes = models.IntegerField(default=0)
    last_hit = models.DateTimeField(null=True)
    last_success = models.DateTimeField(null=True)

    def __str__(self):
        return '{}: {}'.format(self.dictionary.name, self.flashcard.word)

    class Meta:
        verbose_name_plural = 'Dictionary flashcards'

