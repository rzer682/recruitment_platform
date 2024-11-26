from rest_framework import serializers
from .models import Candidat, Recruteur, OffreEmploie, Entreprise

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

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'
