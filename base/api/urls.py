from django.urls import path
from . import views


urlpatterns = [
    path('',  views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
    path('new_room/', views.createRoom),
    path('rooms/<str:pk>/', views.updateRoom),
    path('rooms/<str:pk>/', views.deleteRoom)
]
