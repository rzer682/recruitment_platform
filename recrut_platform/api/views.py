from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsRecruteur
from django_filters.rest_framework import DjangoFilterBackend
from .models import Candidat, Recruteur, OffreEmploie, Entreprise, Candidature, User 
from .serializers import CandidatSerializer, RecruteurSerializer, OffreEmploieSerializer, EntrepriseSerializer, CandidatureSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    

class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    permission_classes = [IsAuthenticated]
    

class RecruteurViewSet(viewsets.ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer
    permission_classes = [IsAuthenticated]

class OffreEmploieViewSet(viewsets.ModelViewSet):
    queryset = OffreEmploie.objects.all()
    serializer_class = OffreEmploieSerializer
    permission_classes = [IsRecruteur, IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titre', 'ville', 'pays', 'date_poste', 'salaire', 'recruteur__entreprise__nom']

    def get_queryset(self):
        return self.queryset
    
    
class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer 
    permission_classes = [IsRecruteur, IsAuthenticated]

    def get_queryset(self):
        return self.queryset

class CandidatureViewSet(viewsets.ModelViewSet):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsRecruteur()]
        return super().get_permissions()
    

class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)