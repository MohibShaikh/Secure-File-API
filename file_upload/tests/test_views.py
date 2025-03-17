import pytest
from django.contrib.auth import get_user_model
from file_upload.models import SecureFile
from rest_framework.test import APIClient
from file_upload.models import User
import hashlib
import tempfile

@pytest.mark.django_db
def test_get_files():
    """Test retrieving files for a user"""
    user = User.objects.create_user(username="testuser", password="testpass")
    file = SecureFile.objects.create(owner=user, file="testfile.txt")

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get("/api/files/")

    assert response.status_code == 200
    assert len(response.data) == 1  # Ensure that one file is returned
    assert response.data[0]["file"] == file.file.name  # Check if the file name matches


@pytest.mark.django_db
def test_get_files():
    """Test retrieving files for a user"""
    user = User.objects.create_user(username="testuser", password="testpass")
    SecureFile.objects.create(owner=user, file="testfile.txt")

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get("/api/files/")

    assert response.status_code == 200
