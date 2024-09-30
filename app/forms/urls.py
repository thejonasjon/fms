from django.urls import path
from .views import FormList, FormDetail, ResponseList, ResponseDetail

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Form Management System API",
        default_version='v1.0',
        description="API documentation for the Form Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jonas.humenu@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('forms/', FormList.as_view(), name='form-list'),
    path('forms/<str:pk>/', FormDetail.as_view(), name='form-detail'),

    path('responses/', ResponseList.as_view(), name='response-list'),
    path('responses/<str:pk>/', ResponseDetail.as_view(), name='response-detail'),

    # Swagger URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]