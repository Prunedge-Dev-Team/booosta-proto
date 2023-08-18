from rest_framework import permissions
from django.core.exceptions import PermissionDenied


class IsAuthenticated(permissions.BasePermission):
    """Allows access only to authenticated users"""
    message = "Request is from an unauthorized application"

    def has_permission(self, request, view):
        user_auth = getattr(request, 'user_auth', None)
        if user_auth:
            return True
        return False
    

class IsSuperAdmin(permissions.BasePermission):
    """Allows access only to super admin users."""
    message = "Only Super Admins are authorized to perform this action."

    def has_permission(self, request, view):
        user_auth = getattr(request, 'user_auth', None)
        if user_auth:
            roles = user_auth.get('roles', [])
            return 'SUPERADMIN' in roles
        return False


class IsAdmin(permissions.BasePermission):
    """Allows access only to admin users."""

    message = "Only Admins are authorized to perform this action."

    def has_permission(self, request, view):
        user_auth = getattr(request, 'user_auth', None)
        if user_auth:
            roles = user_auth.get('roles', [])
            return 'ADMIN' in roles
        return False


class IsRetailerUser(permissions.BasePermission):
    """Allows access only to talent users."""
    message = "Only Retailer users are authorized to perform this action."

    def has_permission(self, request, view):
        user_auth = getattr(request, 'user_auth', None)
        if user_auth:
            roles = user_auth.get('roles', [])
            return 'RETAILER' in roles
        return False


class IsAgentUser(permissions.BasePermission):
    """Allows access only to talent users."""
    message = "Only Agents users are authorized to perform this action."

    def has_permission(self, request, view):
        user_auth = getattr(request, 'user_auth', None)
        if user_auth:
            roles = user_auth.get('roles', [])
            return 'AGENT' in roles
        return False


class IsAggregatorUser(permissions.BasePermission):
    """Allows access only to talent users."""
    message = "Only Aggregator users are authorized to perform this action."

    def has_permission(self, request, view):
        user_auth = getattr(request, 'user_auth', None)
        if user_auth:
            roles = user_auth.get('roles', [])
            return 'AGGREGATOR' in roles
        return False


# class IsAgentOrAggregatorOrIsAdmin(permissions.BasePermission):
#     """Allows access only to talent users."""
#     message = "Only Agents users are authorized to perform this action."

#     def has_permission(self, request, view=None):
#         return bool(
#             request.user
#             and request.user.roles
#             and "AGENT" in request.user.roles
#             or "AGGREGATOR" in request.user.roles
#             or "ADMIN" in request.user.roles
#         )


# class IsAgentOrIsAdmin(permissions.BasePermission):
#     """Allows access only to talent users."""

#     message = "Only Agents users are authorized to perform this action."

#     def has_permission(self, request, view=None):
#         return bool(
#             request.user
#             and request.user.roles
#             and "AGENT" in request.user.roles
#             or "ADMIN" in request.user.roles
#         )

