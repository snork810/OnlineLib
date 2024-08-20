from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
def home(request):
   return render(request, 'djangolib/home.html')

def library(request):
   books = EBooksModel.objects.order_by('author')
   return render(request, 'djangolib/library.html', {'books':books})

def download_file(request, book_id):
    book = get_object_or_404(EBooksModel, id=book_id)
    selected_format = request.POST.get('format', 'txt')

    if selected_format == 'epub':
        file_path = book.epub.path
        content_type = 'application/epub+zip'
        file_name = f"{book.title}.epub"
    elif selected_format == 'fb2':
        file_path = book.fb2.path
        content_type = 'application/x-fictionbook+xml'
        file_name = f"{book.title}.fb2"
    else:
        file_path = book.txt.path
        content_type = 'text/plain'
        file_name = f"{book.title}.txt"

    response = HttpResponse(open(file_path, 'rb'), content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response




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