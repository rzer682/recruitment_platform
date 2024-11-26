from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    experience = models.TextField(blank=True)
    competences = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Recruteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entreprise = models.CharField(max_length=150)
    poste = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.entreprise}"