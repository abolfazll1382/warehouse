# users/permissions.py

import copy

from rest_framework.permissions import BasePermission

from rest_framework.permissions import DjangoModelPermissions


class HasGroupPermission(BasePermission):
    """
    Base permission class to check if a user belongs to required groups.
    If the user is a CEO, they automatically get access to everything.
    """
    required_groups = []

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        # CEO BYPASS: The CEO can do EVERYTHING.
        if request.user.groups.filter(name="CEO").exists():
            return True
            
        # Otherwise check if they belong to the required groups
        return request.user.groups.filter(name__in=self.required_groups).exists()

class IsCEO(HasGroupPermission):
    # We kept this so transfer.py doesn't crash!
    required_groups = ["CEO"]

class CanApprovePurchaseOrder(HasGroupPermission):
    required_groups = ["Purchasing"] 

class CanManagePurchaseOrder(HasGroupPermission):
    required_groups = ["Purchasing"]

class CanReceivePurchaseOrder(HasGroupPermission):
    required_groups = ["WarehouseStaff"]

class StrictModelPermissions(DjangoModelPermissions):
    """
    By default, DRF allows any authenticated user to make GET requests.
    This class forces DRF to check the 'Can view' tick box for GET requests too!
    """
    # 1. Copy the default DRF permissions map
    perms_map = copy.deepcopy(DjangoModelPermissions.perms_map)
    # 2. Force GET requests to require the 'view' permission!
    perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

    def has_permission(self, request, view):
        # 3. CEO BYPASS: If the user is in the CEO group, give them instant access!
        if request.user and request.user.is_authenticated:
            if request.user.groups.filter(name="CEO").exists():
                return True
                
        # Otherwise, check the tick boxes normally
        return super().has_permission(request, view)