from django.shortcuts import render
from .models import *
def home(request):
   return render(request, 'djangolib/home.html')

def library(request):
   books = EBooksModel.objects.order_by('author')
   return render(request, 'djangolib/library.html', {'books':books})

