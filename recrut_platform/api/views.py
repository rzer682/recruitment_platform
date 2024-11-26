from rest_framework import viewsets
from .models import Candidat, Recruteur
from .serializers import CandidatSerializer, RecruteurSerializer


class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    

class RecruteurViewSet(viewsets.ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer
