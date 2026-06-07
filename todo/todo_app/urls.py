from django.urls import path
from .views import TodoViewSet, TypeViewSet

urlpatterns = [
    path('types/', TypeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('types/<int:pk>/', TypeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('todos/', TodoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('todos/<int:pk>/', TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]