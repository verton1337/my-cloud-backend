from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from mainapp.models import File
from mainapp.serializers import FileSerializer

# Create your views here.


class MainView(ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

