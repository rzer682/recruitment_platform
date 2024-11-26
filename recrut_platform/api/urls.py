from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatViewSet, RecruteurViewSet, OffreEmploieViewSet, EntrepriseViewSet, CandidatureViewSet

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet)
router.register(r'recruteurs', RecruteurViewSet)
router.register(r'offre_emploi', OffreEmploieViewSet)
router.register(r'entreprise', EntrepriseViewSet)
router.register(r'candidature', CandidatureViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]