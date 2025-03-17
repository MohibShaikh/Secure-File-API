from django.contrib import admin
from .models import User, SecureFile

# Register User Model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active', 'is_staff')

# Register SecureFile Model
@admin.register(SecureFile)
class SecureFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'encrypted_name', 'uploaded_at')
    search_fields = ('owner__username', 'encrypted_name')
    list_filter = ('uploaded_at',)
