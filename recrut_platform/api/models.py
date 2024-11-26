from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    experience = models.TextField(blank=True)
    competences = models.TextField(blank=True, null=True)  
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True) 
    
    

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    poste = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.user} - {self.entreprise}"
    

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
    offre = models.ForeignKey(OffreEmploie, on_delete=models.CASCADE)
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
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

    lettre_motivation = models.FileField(upload_to='lettre_motivation/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.candidat} - {self.offre}"