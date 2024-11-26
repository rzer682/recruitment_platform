from rest_framework import viewsets
from .models import Candidat, Recruteur, OffreEmploie
from .serializers import CandidatSerializer, RecruteurSerializer, OffreEmploieSerializer


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