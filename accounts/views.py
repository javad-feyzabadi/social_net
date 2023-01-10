from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView

from . serializers import RegisterSerializer

User = get_user_model()

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
