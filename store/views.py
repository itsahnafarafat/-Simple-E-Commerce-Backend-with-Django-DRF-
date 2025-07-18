from rest_framework import viewsets, filters
from .models import Product, CartItem, Order, OrderItem
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        # Create order from cart items
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items:
            return Response({'detail': 'Cart is empty'}, status=400)
        
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
        cart_items.delete() # Clear cart
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['in_stock']
    search_fields = ['name', 'description']
    