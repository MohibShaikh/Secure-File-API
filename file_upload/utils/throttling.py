from rest_framework.throttling import UserRateThrottle

class FileUploadThrottle(UserRateThrottle):
    """Custom throttle class for file uploads."""
    scope = 'file_upload'
