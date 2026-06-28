from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product
from .serializers import ProductSerializer
from users.permissions import StrictModelPermissions

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, StrictModelPermissions]
    
    # Add filtering and searching for products!
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active', 'unit']
    search_fields = ['sku', 'name', 'barcode', 'description']