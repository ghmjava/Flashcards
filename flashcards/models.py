from django.db import models

class User(models.Model):
    login  = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    registered = models.DateTimeField()
    last_login = models.DateTimeField()

    def __str__(self):
        return self.login

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
    created = models.DateTimeField()

    def __str__(self):
        return self.word

class Dictionary(models.Model):
    name = models.CharField(max_length=20)
    owner  = models.ForeignKey(User)
    created = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dictionaries'

class Dictionary_Flashcard(models.Model):
    dictionary = models.ForeignKey(Dictionary)
    flashcard = models.ForeignKey(Flashcard)
    hits = models.IntegerField()
    successes = models.IntegerField()
    last_hit = models.DateTimeField()
    last_success = models.DateTimeField()

    def __str__(self):
        return '{}: {}'.format(self.dictionary.name, self.flashcard.word)

    class Meta:
        verbose_name_plural = 'Dictionary flashcards'

