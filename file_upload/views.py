from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import SecureFile
from .serializers import SecureFileSerializer
from file_upload.utils.encryption import encrypt_file,decrypt_file
from django.http import FileResponse
from file_upload.utils.permissions import IsOwnerOrAdmin
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from file_upload.utils.auth_utils import generate_tokens
from django.contrib.auth import get_user_model
User = get_user_model() 


class SecureFileViewSet(viewsets.ModelViewSet):
    queryset = SecureFile.objects.all()
    serializer_class = SecureFileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]

    # def create(self, request, *args, **kwargs):
    #     """
    #     Handle file upload logic here.

    #     This method automatically associates the file with the currently authenticated user.
    #     """
    #     file = request.FILES.get('file')  # Use .get() to avoid KeyError
        
    #     if file:
    #     # Save the file first (without encryption)
    #         secure_file = SecureFile(owner=request.user, file=file)
    #         secure_file.save()  # Save the uploaded file to the database
            
    #         # Encrypt the file content
    #         encrypt_file(secure_file.file.path)
            
    #         return Response({'message': 'File uploaded and encrypted successfully!'}, status=status.HTTP_201_CREATED)
        
    #     return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        # print("Incoming request headers:", request.headers)  # Log request headers
        # print("Incoming request body:", request.body)  # Log request body (for debugging)
        print("Incoming request files:", request.FILES)  # Log request files

        file = request.FILES.get('file')  # Retrieve the file from the request
        print(f'user is {type(request.user)}')
        if file:
            print(f"File received: {file.name}")  # Log the file name   
            # Save the file to the database
            secure_file = SecureFile(owner=request.user, file=file)
            
            secure_file.save()

            # Log the file path
            print(f"File saved at: {secure_file.file.path}")

            # Encrypt the file
            encrypt_file(secure_file.file.path)
            print("File encrypted successfully")

            return Response({'message': 'File uploaded and encrypted successfully!'}, status=status.HTTP_201_CREATED)
        
        print("No file provided in the request")  # Log if no file is provided
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, *args, **kwargs):
        file_obj = self.get_object()  # Get the file object

        # Decrypt the file and get the path to the decrypted file
        decrypted_file_path = decrypt_file(file_obj.file.path)

        # Serve the decrypted file to the user
        try:
            with open(decrypted_file_path, 'rb') as f:
                response = FileResponse(f, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{file_obj.file.name}"'
                return response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        """
        Filter files based on the user role.
        """
        if self.request.user.is_staff:
            return SecureFile.objects.all()  # Admin can view all files
        return SecureFile.objects.filter(owner=self.request.user)  # Non-admin can only see their own files

    def has_object_permission(self, request, view, obj):
        """
        Ensure that the user has permission to access or modify the object.
        """
        return obj.owner == request.user or request.user.is_staff

    @action(detail=True, methods=['post'])
    def encrypt_file(self, request, pk=None):
        """
        Endpoint to encrypt a file.

        This action allows the user to encrypt a file. The encryption method needs to 
        be defined and executed before saving the file.
        """
        file_obj = self.get_object()
        # Encrypt the file and save the encrypted version (Ensure encrypt_file handles this)
        encrypt_file(file_obj.file.path)
        return Response({'message': 'File encrypted successfully'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def upload_file(self, request):
        """
        Upload a file to the server.
        
        This is now redundant as the `create` method already handles uploads.
        You can remove this method if you don't need it anymore.
        """
        return self.create(request) 
    
class TokenView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'])
    def refresh(self, request):
        """Refresh token for authenticated users"""
        tokens = generate_tokens(request.user)
        return Response(tokens)
