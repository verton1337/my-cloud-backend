from rest_framework import serializers
from mainapp.models import File
class FileSerializer(serializers.ModelSerializer):
    # userName = serializers.CharField(max_length=64)
    # phone = serializers.CharField(max_length=20)
 
    class Meta:
        model = File
        fields = ['title', 'url', 'id']