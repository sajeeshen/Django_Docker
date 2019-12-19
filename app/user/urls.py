from rest_framework.routers import DefaultRouter
from .views import UserCreateViewSet, CreateTokenView
from django.urls import path, include

app_name = 'user'


urlpatterns = [
    path('user/create/', UserCreateViewSet.as_view()),
    path('user/login/', CreateTokenView.as_view()),
]
