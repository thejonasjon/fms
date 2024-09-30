from django.urls import path
from .views import FormList, FormDetail, ResponseList, ResponseDetail

urlpatterns = [
    path('forms/', FormList.as_view(), name='form-list'),
    path('forms/<str:pk>/', FormDetail.as_view(), name='form-detail'),

    path('responses/', ResponseList.as_view(), name='response-list'),
    path('responses/<str:pk>/', ResponseDetail.as_view(), name='response-detail'),
]