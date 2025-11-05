from rest_framework import generics
from ..serializer import RegisterSerializer
from ..models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer