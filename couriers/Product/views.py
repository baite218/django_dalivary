from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Product.models import product,category
from Product.permissions import IsProductOwnerOrReadOnly
from Product.serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductView(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = (IsProductOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend)
    filter_class = ['category']

class CategoryView(ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    permission_classes = (IsProductOwnerOrReadOnly, )
    