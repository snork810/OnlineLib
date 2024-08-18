from django.shortcuts import render, redirect
from .models import NoModeratedBooksModel
from .forms import NoModeratedBooksModelForm


# Create your views here.
def bookshelf(request):
    return render(request, 'books/bookshelf.html')


def addbook(request):
    error = ''
    if request.method == "POST":
        form = NoModeratedBooksModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library')
        else:
            error = 'Форма была заполнена некорректно'

    form = NoModeratedBooksModelForm()
    context = {'form': form,
               'error': error
               }
    return render(request, 'books/addbook.html', context)
