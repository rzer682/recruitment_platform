from rest_framework import serializers
from .models import Candidate, Recruiter, JobOffer, Company, Application, User 


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
        if role == 'candidate': 
            Candidate.objects.create(user=user)
        elif role == 'recruiter':
            Recruiter.objects.create(user=user)
        return user
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'