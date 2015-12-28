from rest_framework import serializers
from .models import Flashcard, Dictionary
from flashcards.models import Language, Dictionary_Flashcard
from django.contrib.auth.models import User

class FlashcardSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField()
    dictionaries = serializers.HyperlinkedRelatedField(many=True, view_name='dictionary-detail', read_only=True)
    class Meta:
        model = Flashcard
        fields = ('id', 'word', 'translation', 'language', 'translation_language', 'owner', 'created', 'dictionaries')

class SimpleFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'word', 'translation')

class ReadDictionarySerializer(serializers.ModelSerializer):
#     owner = serializers.HyperlinkedIdentityField(many=False, view_name='user-detail')
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
#     flashcards = serializers.HyperlinkedRelatedField(many=True, view_name='flashcard-detail', queryset=Flashcard.objects.all())
#     flashcards = serializers.SlugRelatedField(many=True, slug_field='word', queryset=Flashcard.objects.all())
    flashcards = SimpleFlashcardSerializer(many=True)
    created = serializers.DateTimeField()

    class Meta:
        model = Dictionary
        fields = ('id', 'name', 'description', 'owner', 'created', 'flashcards')

class WriteDictionarySerializer(serializers.ModelSerializer):
#     owner = serializers.HyperlinkedIdentityField(many=False, view_name='user-detail')
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    flashcards = serializers.HyperlinkedRelatedField(many=True, view_name='flashcard-detail', queryset=Flashcard.objects.all())
#     flashcards = serializers.SlugRelatedField(many=True, slug_field='word', queryset=Flashcard.objects.all())
#     flashcards = FlashcardSerializer(many=True)
    created = serializers.DateTimeField()

    class Meta:
        model = Dictionary
        fields = ('id', 'name', 'description', 'owner', 'created', 'flashcards')

    def create_or_update(self, db_dict, validated_data):

        db_dict.name = validated_data.pop('name')
        db_dict.name = validated_data.pop('description')
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

    def create(self, validated_data):

        db_dict = Dictionary()
        db_dict.owner = validated_data.pop('owner')
        return self.create_or_update(db_dict, validated_data)

    def update(self, instance, validated_data):
        db_dict = Dictionary.objects.filter(id=instance.id).first()
        return self.create_or_update(db_dict, validated_data)
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    dictionaries = serializers.HyperlinkedRelatedField(many=True, view_name='dictionary-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'dictionaries')

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'code', 'name', 'description')
