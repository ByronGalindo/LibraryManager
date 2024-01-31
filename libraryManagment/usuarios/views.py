from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsAdmin, IsLibrarianOrAdmin, IsClientOrAdmin, IsOwnerOrAdmin

class AdminUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]

    def perform_create(self, serializer):
        serializer.save(user_type=CustomUser.ADMIN)

class AdminUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type=CustomUser.ADMIN)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]

class AdminUserListAllView(generics.ListAPIView):
    queryset = CustomUser.objects.all().exclude(is_superuser=True)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]

class LibrarianUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsLibrarianOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user_type=CustomUser.LIBRARIAN)

class LibrarianUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type=CustomUser.LIBRARIAN)
    serializer_class = CustomUserSerializer
    permission_classes = [IsLibrarianOrAdmin]

class ClientUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(user_type=CustomUser.CLIENT)

class ClientUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type=CustomUser.CLIENT)
    serializer_class = CustomUserSerializer
    permission_classes = [IsLibrarianOrAdmin]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrAdmin]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Verificar si el usuario que realiza la actualización es un administrador
        if not (request.user.user_type == CustomUser.ADMIN or 'user_type' not in request.data):
            return Response({'detail': 'No tienes permisos para actualizar el tipo de usuario.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class MeUserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user