from django.shortcuts import render
from rest_framework import viewsets

from .Serializers import UserSerializer
from .models import User


class UsersViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

