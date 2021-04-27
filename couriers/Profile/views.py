# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.viewsets import ModelViewSet

from Profile.models import User
from Profile.permissions import IsUserOwnerOrReadOnly
from Profile.serializers import ProfileSerializer


# class ProfileView(ModelViewSet):
#     queryset = User.objects.prefetch_related('order')
#     serializer_class = ProfileSerializer
#     lookup_field = 'pk'
#     permission_classes = (IsUserOwnerOrReadOnly, )



# class UserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer

from rest_auth.models import TokenModel
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from django.contrib.auth import authenticate


class ProfileRegisterView(CreateAPIView):
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('success', status=status.HTTP_201_CREATED)


class ProfileLoginView(GenericAPIView):
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token = TokenModel.objects.get(user=user)
            return Response({'key': token.key}, status=status.HTTP_201_CREATED)
        return Response('invalid login', status=status.HTTP_401_UNAUTHORIZED)

