import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from file_upload.models import User

@pytest.mark.django_db
def test_unauthenticated_access():
    """Test accessing an API endpoint without authentication"""
    client = APIClient()
    
    # Try accessing the endpoint without setting credentials
    response = client.get(reverse("file_upload-list"))  # Adjusted to match the name generated by the router
    assert response.status_code == 401  # Unauthorized
    
    # You can check the response message if needed
    assert response.data == {"detail": "Authentication credentials were not provided."}


@pytest.mark.django_db
def test_unauthenticated_access():
    """Test accessing an API endpoint without authentication"""
    client = APIClient()
    
    # Try accessing the endpoint without setting credentials
    response = client.get(reverse("file_upload-list"))  # This is the correct URL name
    
    # Assert that the response status is 401 Unauthorized
    assert response.status_code == 401  # Unauthorized
    
    # Assert that the response contains the expected error message
    assert response.data == {"detail": "Authentication credentials were not provided."}
