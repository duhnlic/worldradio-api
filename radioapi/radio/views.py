from django.shortcuts import render
from .models import Radio
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RadioSerializer
class RadioViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Radio.objects.all()
    # The serializer class for serializing output
    serializer_class = RadioSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
