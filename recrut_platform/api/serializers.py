from rest_framework import serializers
from .models import Candidat, Recruteur, OffreEmploie, Entreprise, Candidature, User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'role']
        
    def create(self, validated_data):
        role = validated_data.get('role')
        user = User.objects.create(**validated_data)
        if role == 'candidat':
            Candidat.objects.create(user=user)
        elif role == 'recruteur':
            Recruteur.objects.create(user=user)
        return user
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

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = '__all__'