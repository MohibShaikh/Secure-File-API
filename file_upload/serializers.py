from rest_framework import serializers
from .models import SecureFile

class SecureFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFile
        fields = ['id', 'owner', 'file', 'encrypted_name', 'uploaded_at']
