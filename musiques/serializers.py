from .models import Morceau, Artiste
from rest_framework import serializers

class MorceauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morceau
        fields = ['id','titre','artiste','date_sortie']

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['nom']