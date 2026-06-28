# sales/views.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

from sales.models import SalesOrder
from sales.serializers import SalesOrderSerializer
from sales.services import ship_sales_order


class SalesOrderViewSet(ModelViewSet):
    serializer_class = SalesOrderSerializer
    permission_classes = [IsAuthenticated,] # Everyone logged in can access this endpoint

    def get_queryset(self):
        """
        THE 3-TIER DATA ISOLATION LOGIC
        """
        user = self.request.user
        
        # TIER 1: Is it the CEO? Return EVERYTHING.
        if user.groups.filter(name="CEO").exists():
            return SalesOrder.objects.all().order_by('-created_at')
            
        # TIER 2: Is it an Employee? (They have an EmployeeProfile)
        if hasattr(user, 'employee_profile'):
            employee = user.employee_profile
            # Employees only see orders for Warehouses they are ticked/allowed to access!
            allowed_warehouses = employee.accessible_warehouses.all()
            return SalesOrder.objects.filter(warehouse__in=allowed_warehouses).order_by('-created_at')
            
        # TIER 3: It must be a Customer! (They have a CustomerProfile)
        if hasattr(user, 'customer_profile'):
            # Customers ONLY see their own orders. They cannot see other customers' orders!
            customer = user.customer_profile
            return SalesOrder.objects.filter(customer=customer).order_by('-created_at')

        # Fallback security: If they have neither profile, return nothing.
        return SalesOrder.objects.none()

    @action(detail=True, methods=['post'])
    def ship(self, request, pk=None):
        """
        Custom endpoint for employees to ship an order.
        URL: /api/sales-orders/{id}/ship/
        """
        sales_order = self.get_object()
        
        # Only Employees (and CEO) should be able to ship an order, not customers!
        if not hasattr(request.user, 'employee_profile') and not request.user.groups.filter(name="CEO").exists():
            return Response({"error": "Customers cannot ship orders."}, status=status.HTTP_403_FORBIDDEN)

        try:
            # Re-use your professional service logic here!
            ship_sales_order(sales_order=sales_order, performed_by=request.user)
            return Response({"message": "Order shipped and inventory deducted successfully!"})
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)