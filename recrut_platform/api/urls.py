from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatViewSet, RecruteurViewSet, OffreEmploieViewSet, EntrepriseViewSet, CandidatureViewSet, UserViewSet

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet)
router.register(r'recruteurs', RecruteurViewSet)
router.register(r'offre_emploi', OffreEmploieViewSet)
router.register(r'entreprise', EntrepriseViewSet)
router.register(r'candidature', CandidatureViewSet)
router.register(r'utilisateurs', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]