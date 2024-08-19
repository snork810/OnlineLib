from django.shortcuts import render, redirect
from .models import NoModeratedBooksModel
from .forms import NoModeratedBooksModelForm


from django.contrib.auth.decorators import login_required

from djangolib.models import FavouriteBook

# С УТРА ПОПРОБОВАТЬ СЛИТЬ BOOKS И DJANGOLIB В ОДНО ПРИЛОЖЕНИЕ
@login_required
def bookshelf(request):
    files = NoModeratedBooksModel.objects.all()
    favorites = FavouriteBook.objects.filter(user=request.user)
    context = {
        'files': files,
        'favorites': favorites
    }
    return render(request, 'books/bookshelf.html', context)


def addbook(request):
    error = ''
    if request.method == "POST":
        form = NoModeratedBooksModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bookshelf')
        else:
            error = 'Форма была заполнена некорректно'

    form = NoModeratedBooksModelForm()
    context = {'form': form,
               'error': error
               }
    return render(request, 'books/addbook.html', context)



def file_detail(request, pk):
    file_instance = NoModeratedBooksModel.objects.get(pk=pk)
    with file_instance.txt.open('r') as f:
        content = f.read()
    return render(request, 'books/file_detail.html', {'content': content})
