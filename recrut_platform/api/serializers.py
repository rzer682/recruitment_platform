from rest_framework import serializers
from .models import Candidat, Recruteur, OffreEmploie

class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = '__all__'

class RecruteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruteur
        fields = '__all__'


class OffreEmploieSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffreEmploie
        fields = '__all__'