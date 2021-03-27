from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from .serializers import UserSerializer
from rest_framework import generics

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 