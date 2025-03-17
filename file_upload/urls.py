from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SecureFileViewSet, TokenView
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from secure_file_api import settings as SETTINGS_MODULE

router = DefaultRouter()
router.register(r'files', SecureFileViewSet, basename='file_upload')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]

if SETTINGS_MODULE.DEBUG:
    urlpatterns += static(SETTINGS_MODULE.MEDIA_URL, document_root=SETTINGS_MODULE.MEDIA_ROOT)