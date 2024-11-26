
from rest_framework.permissions import BasePermission
class IsRecruteur(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'recruteur'