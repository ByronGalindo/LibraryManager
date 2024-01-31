# urls.py
from django.urls import path
from .views import (
    AdminUserCreateView,
    AdminUserListAllView,
    AdminUserListView,
    LibrarianUserCreateView,
    LibrarianUserListView,
    ClientUserCreateView,
    ClientUserListView,
    MeUserDetailView,
    UserDetailView,
)

urlpatterns = [
    # Admin views
    path('users/administrator/users/create/', AdminUserCreateView.as_view(), name='admin-user-create'),
    path('users/administrator/users/all', AdminUserListAllView.as_view(), name='all-user-list'),
    path('users/administrator/users/', AdminUserListView.as_view(), name='admin-user-list'),

    # Librarian views
    path('users/librarian/users/create/', LibrarianUserCreateView.as_view(), name='librarian-user-create'),
    path('users/librarian/users/', LibrarianUserListView.as_view(), name='librarian-user-list'),

    # Client views
    path('users/client/users/create/', ClientUserCreateView.as_view(), name='client-user-create'),
    path('users/client/users/', ClientUserListView.as_view(), name='client-user-list'),

    # User detail view
    path('users/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/users/me/', MeUserDetailView.as_view(), name='me-user-detail'),
]
