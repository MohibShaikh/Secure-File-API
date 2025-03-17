import pytest
from django.contrib.auth import get_user_model
import hashlib
from file_upload.models import SecureFile

from file_upload.models import User

@pytest.mark.django_db
def test_user_creation():
    """Test creating a user with role field"""
    user = User.objects.create_user(username="testuser", password="testpass")
    assert user.username == "testuser"
    assert user.check_password("testpass")

@pytest.mark.django_db
def test_secure_file_creation():
    """Test creating a SecureFile and assigning to a user"""
    user = User.objects.create_user(username="testuser", password="testpass")
    file_obj = SecureFile.objects.create(owner=user, file="testfile.txt")

    assert file_obj.owner == user
    assert file_obj.encrypted_name == hashlib.sha256("testfile.txt".encode()).hexdigest()
