from rest_framework import viewsets
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only the current user's cart items
        return CartItem.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Auto-assign the logged-in user
        serializer.save(user=self.request.user)