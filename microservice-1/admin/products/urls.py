from django.contrib import admin
from django.urls import path

from .views import ProductViewSet, UserAPIView, UserViewSet

urlpatterns = [

    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    path('products/<str:pk>/like', ProductViewSet.as_view({
        'post': 'like',
    })),

    path('user', UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('user/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    

    path('user', UserAPIView.as_view())
]
