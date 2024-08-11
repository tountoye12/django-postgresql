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
    path('employee', views.get_all_employee),
    path('employee/add', views.add_user),
    path("employee/get/<int:pk>/", views.get_employee),
    path("employee/delete/<int:pk>/", views.delete_employee),

    



    path('group', views.get_all_group),
    path('group/add', views.add_group),
    path('group/get/<int:pk>/', views.get_group),
    path('group/delete/<int:pk>/', views.delete_group),


    
]