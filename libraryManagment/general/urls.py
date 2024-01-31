from django.urls import path
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Library Manager",
        default_version='v1',
        description="API for manage the library service",
        terms_of_service="https://www.tu-api.com/terms/",
        contact=openapi.Contact(email="bahegasu2000@gmail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('library_Manager/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('library_Manager/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('library_Manager/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]