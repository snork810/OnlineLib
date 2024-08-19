from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
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

@login_required
def add_to_favorites(request, book_id):
    book = EBooksModel.objects.get(id=book_id)
    if request.method == 'POST':
        favorite_book = FavouriteBook(user=request.user, book=book)
        favorite_book.save()
        return redirect('bookshelf')  # Убедитесь, что путь 'bookshelf' прописан в urls

    return render(request, 'djangolib/library.html', {'book': book})