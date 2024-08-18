from django.shortcuts import render
from .models import *
def home(request):
   return render(request, 'djangolib/home.html')

def library(request):
   books = EBooksModel.objects.order_by('author')
   return render(request, 'djangolib/library.html', {'books':books})


def file_detail_lib(request, pk):
   file_instance = EBooksModel.objects.get(pk=pk)
   with file_instance.txt.open('r') as f:
      content = f.read()
   return render(request, 'djangolib/file_detail_lib.html', {'content': content})
