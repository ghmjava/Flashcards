from rest_framework import serializers
from .models import Flashcard, Dictionary
from flashcards.models import Language
from django.contrib.auth.models import User

class FlashcarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'word', 'translation', 'language', 'translation_language', 'owner', 'created')

class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    details = serializers.HyperlinkedRelatedField(source="id", many=False, view_name='dictionary-detail', read_only=True)
    class Meta:
        model = Dictionary
        fields = ('id', 'name', 'description', 'owner', 'created', 'details')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    dictionaries = serializers.HyperlinkedRelatedField(many=True, view_name='dictionary-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'dictionaries')

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'code', 'name', 'description')
