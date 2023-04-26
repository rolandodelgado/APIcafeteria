from rest_framework import permissions
    
class IsRecepcionista(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.get().name == 'recepcionista'
    
class IsCocinero(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.get().name == 'cocinero'
    
class IsRecepcionistaOrCocinero(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.user.groups.get().name
        return role == 'recepcionista' or role == 'cocinero'