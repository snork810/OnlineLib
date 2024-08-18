"""
URL configuration for DjangoLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from djangolib import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('library/', views.library, name='library'),
    path('library/files/<int:pk>/', views.file_detail_lib, name='file_detail_lib'),
    path('bookshelf/', include('books.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)