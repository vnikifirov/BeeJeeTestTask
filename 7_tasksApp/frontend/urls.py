from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('create', index),
    path('edit', index),
    path('login', index),
]