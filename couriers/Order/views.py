from django.shortcuts import render

from Order.models import Order
from Order.permissions import IsOrderOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet


from Order.serializers import OrderSerializer

class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    permission_classes = (IsOrderOwnerOrReadOnly,)

# from rest_auth.models import TokenModel
# from rest_framework import status
# from rest_framework.generics import CreateAPIView, GenericAPIView
# from rest_framework.response import Response

# from Order.serializers import OrderSerializer
# from django.contrib.auth import authenticate

# class 

