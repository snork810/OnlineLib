from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bookshelf, name='bookshelf'),
    path('addbook/', views.addbook, name='addbook'),
    path('files/<int:pk>/', views.file_detail, name='file_detail'),
]