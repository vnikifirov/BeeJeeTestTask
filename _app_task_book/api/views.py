from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from .serializers import UserSerializer
from rest_framework import generics

# Create your views here.
# def main(request):
#     return HttpResponse('<h1>Hello</h1>')

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 