from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    ROLES = (
        ('recruteur', 'Recruteur'),
        ('candidat', 'Candidat'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='candidat')

    def __str__(self):
        return self.username

    

class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, default=1)
    telephone = models.CharField(max_length=15, blank=True)
    experience = models.TextField(blank=True)
    competences = models.TextField(blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    lettre_motivation = models.FileField(upload_to='lettre_motivation/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

class Entreprise(models.Model):
    nom = models.CharField(max_length=150)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.nom
    
class Recruteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, default=1)
    entreprise = models.ForeignKey('Entreprise', on_delete=models.CASCADE)
    poste = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.entreprise.nom}"
    

class OffreEmploie(models.Model): 
    recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_poste = models.DateField()
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.titre
    

class Candidature(models.Model):
    offre = models.ForeignKey('OffreEmploie', on_delete=models.CASCADE, related_name='candidatures')
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE, related_query_name='candidatures')
    date_candidature = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'en_attente'),
            ('vue', 'vue'),
            ('accepter', 'accepter'),
            ('rejeter', 'rejeter'),
        ],
        default='en_attente'
    )
    lettre_motivation = models.FileField(upload_to='lettre_motivation/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.candidate.user.first_name} {self.candidate.user.last_name} - {self.job_offer.title}"
