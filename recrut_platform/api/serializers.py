from rest_framework import serializers
from .models import Candidat, Recruteur, OffreEmploie, Entreprise, Candidature, User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        role = validated_data.get('role', None)
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password: 
            user.set_password(password)
        user.save()
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