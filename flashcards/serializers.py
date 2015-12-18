from rest_framework import serializers
from .models import Flashcard, Dictionary
from flashcards.models import Language, Dictionary_Flashcard
from django.contrib.auth.models import User

class FlashcardSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.ReadOnlyField()
    dictionaries = serializers.HyperlinkedRelatedField(many=True, view_name='dictionary-detail', read_only=True)
    class Meta:
        model = Flashcard
        fields = ('id', 'word', 'translation', 'language', 'translation_language', 'owner', 'created', 'dictionaries')

class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    details = serializers.HyperlinkedRelatedField(source="id", many=False, view_name='dictionary-detail', read_only=True)
    flashcards = serializers.HyperlinkedRelatedField(many=True, view_name='flashcard-detail', queryset=Flashcard.objects.all())

    created = serializers.ReadOnlyField()
    class Meta:
        model = Dictionary
        fields = ('id', 'name', 'description', 'owner', 'created', 'details', 'flashcards')

    def update(self, instance, validated_data):
        db_dict = Dictionary.objects.filter(id=instance.id).first()
        db_dict.name = validated_data.pop('name')
        db_dict.save()
        flashcard_data = validated_data.pop('flashcards')
        Dictionary_Flashcard.objects.filter(dictionary__id=db_dict.id).delete()
        for flashcard in flashcard_data:
            df = Dictionary_Flashcard()
            df.dictionary = db_dict
            db_flashcard = Flashcard.objects.filter(id=flashcard.id).first()
            df.flashcard = db_flashcard
            df.save()
        return db_dict

class UserSerializer(serializers.HyperlinkedModelSerializer):
    dictionaries = serializers.HyperlinkedRelatedField(many=True, view_name='dictionary-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'dictionaries')

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'code', 'name', 'description')
