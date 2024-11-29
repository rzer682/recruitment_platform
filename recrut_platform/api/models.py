from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    ROLES = (
        ('recruiter', 'Recruiter'),
        ('candidate', 'Candidate'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='candidate')

    def __str__(self):
        return self.username

    

class Candidate(models.Model):
    user = models.OneToOneField('api.User', on_delete=models.CASCADE, null=False, default=1)
    phone_number = models.CharField(max_length=15, blank=True)
    experience = models.TextField(blank=True)
    skills = models.TextField(blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    cover_lettre = models.FileField(upload_to='cover_lettre/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

class Company(models.Model):
    name = models.CharField(max_length=150)
    addresse = models.CharField(max_length=200)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name
    
class Recruiter(models.Model):
    user = models.OneToOneField('api.User', on_delete=models.CASCADE, null=False, default=1)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"
    

class JobOffer(models.Model): 
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_poste = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    addresse = models.CharField(max_length=200)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Application(models.Model):
    job = models.ForeignKey('JobOffer', on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_query_name='applications')
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'pending'),
            ('seen', 'seen'),
            ('accepted', 'accepted'),
            ('rejected', 'rejected'),
        ],
        default='pending'
    )
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.candidate.user.first_name} {self.candidate.user.last_name} - {self.job.title}"
