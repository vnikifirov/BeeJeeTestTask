from django.urls import path
from .views import UserView

urlpatterns = [
    path('create', UserView.as_view()),
]