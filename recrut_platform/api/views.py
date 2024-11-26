from rest_framework import viewsets
from .models import Candidat, Recruteur, OffreEmploie, Entreprise
from .serializers import CandidatSerializer, RecruteurSerializer, OffreEmploieSerializer, EntrepriseSerializer


class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    

class RecruteurViewSet(viewsets.ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer

class OffreEmploieViewSet(viewsets.ModelViewSet):
    queryset = OffreEmploie.objects.all()
    serializer_class = OffreEmploieSerializer

    def get_queryset(self):
        return self.queryset
    
class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer 

    def get_queryset(self):
        return self.queryset
