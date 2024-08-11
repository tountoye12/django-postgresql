from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(

    openapi.Info(
        title = "Employee Api",
        default_version = 'v1',
        description="API documentation description",
    ), 
    public=True,
    permission_classes=[permissions.AllowAny]
)

from . import views

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('employees/', views.get_all_employee),
    path('employees/add', views.add_user),
    path("employees/get/<int:pk>/", views.get_employee),
    path("employees/delete/<int:pk>/", views.delete_employee),

    path('groups', views.get_all_group),
    path('groups/add', views.add_group),
    path('groups/get/<int:pk>/', views.get_group),
    path('groups/delete/<int:pk>/', views.delete_group),
    
]