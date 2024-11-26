from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatViewSet, RecruteurViewSet

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet)
router.register(r'recruteurs', RecruteurViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]