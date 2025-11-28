from django.urls import reverse_lazy
from .models import Morceau, Artiste
from .serializers import MorceauSerializer, ArtisteSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class MorceauViewSet(viewsets.ModelViewSet):
    queryset = Morceau.objects.all()
    serializer_class = MorceauSerializer
    permission_classes = [IsAuthenticated]

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    #permission_classes = [IsAuthenticated]