# users/views/customer_auth.py

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers.customer_auth import CustomerRegistrationSerializer

class CustomerRegistrationView(GenericAPIView):
    # AllowAny allows public users (not logged in) to access this endpoint
    permission_classes = [AllowAny]
    serializer_class = CustomerRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        return Response(
            {
                "message": "Customer account created successfully.",
                "username": user.username,
                "email": user.email
            },
            status=status.HTTP_201_CREATED
        )