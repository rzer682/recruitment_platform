from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, CandidateViewSet, RecruiterViewSet, JobOfferViewSet, CompanyViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'candidates', CandidateViewSet)
router.register(r'recruiters', RecruiterViewSet)
router.register(r'job_offers', JobOfferViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', lambda request: JsonResponse({"message": "Welcome to my recruitment API!"})),
    path('inscription/', UserViewSet.as_view({'post': 'create'})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]