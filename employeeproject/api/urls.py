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
    path('allemployee', views.get_all_employee),
    path('addemployee', views.add_user),
    path('allgroup', views.get_all_group),
    path('addgroup', views.add_group),
    path('allgroup/<int:pk>', views.get_group),
    path('deletegroup/<int:pk>/', views.delete_group),


    
]