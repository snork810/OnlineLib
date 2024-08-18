from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bookshelf, name='bookshelf'),
    path('addbook/', views.addbook, name='addbook'),
]