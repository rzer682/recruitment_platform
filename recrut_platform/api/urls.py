from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CandidatViewSet, RecruteurViewSet, OffreEmploieViewSet, EntrepriseViewSet, CandidatureViewSet, UserViewSet

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet)
router.register(r'recruteurs', RecruteurViewSet)
router.register(r'offre_emploi', OffreEmploieViewSet)
router.register(r'entreprise', EntrepriseViewSet)
router.register(r'candidature', CandidatureViewSet)

urlpatterns = [
    path('', lambda request: JsonResponse({"message": "API de Recrutement!"})),
    path('inscription/', UserViewSet.as_view({'post': 'create'})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]