from django.contrib import admin
from .models import Candidat, Recruteur, OffreEmploie, Candidature, Entreprise

# Register your models here.

admin.site.register(Candidat)
admin.site.register(Recruteur)
admin.site.register(OffreEmploie)
admin.site.register(Candidature)
admin.site.register(Entreprise)