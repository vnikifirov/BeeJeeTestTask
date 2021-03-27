from django.urls import path
from .views import UserView

urlpatterns = [
    path('', UserView.as_view()),
    path('home', UserView.as_view()),
]