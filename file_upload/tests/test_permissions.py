import pytest
from django.contrib.auth import get_user_model
from file_upload.models import SecureFile
from file_upload.utils.permissions import IsOwnerOrAdmin
from rest_framework.permissions import SAFE_METHODS
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from file_upload.models import User

@pytest.mark.django_db
def test_file_owner_permission():
    """Test that only the owner or admin can access the file"""
    user1 = User.objects.create_user(username="user1", password="testpass")
    user2 = User.objects.create_user(username="user2", password="testpass")
    admin = User.objects.create_superuser(username="admin", password="adminpass")


    secure_file = SecureFile.objects.create(owner=user1, file="testfile.txt")

    request_factory = APIRequestFactory()
    request = request_factory.get("/")
    request.user = user1

    permission = IsOwnerOrAdmin()
    assert permission.has_object_permission(request, None, secure_file) is True

    request.user = user2
    assert permission.has_object_permission(request, None, secure_file) is False

    request.user = admin
    assert permission.has_object_permission(request, None, secure_file) is True
