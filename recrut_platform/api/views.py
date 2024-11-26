from rest_framework import viewsets
from .permissions import IsRecruteur
from django_filters.rest_framework import DjangoFilterBackend
from .models import Candidat, Recruteur, OffreEmploie, Entreprise, Candidature, User 
from .serializers import CandidatSerializer, RecruteurSerializer, OffreEmploieSerializer, EntrepriseSerializer, CandidatureSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    

class RecruteurViewSet(viewsets.ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer

class OffreEmploieViewSet(viewsets.ModelViewSet):
    queryset = OffreEmploie.objects.all()
    serializer_class = OffreEmploieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titre', 'ville', 'pays', 'date_poste', 'salaire', 'recruteur__entreprise__nom']

    def get_queryset(self):
        return self.queryset
    
    
class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer 

    def get_queryset(self):
        return self.queryset

class CandidatureViewSet(viewsets.ModelViewSet):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsRecruteur()]
        return super().get_permissions()