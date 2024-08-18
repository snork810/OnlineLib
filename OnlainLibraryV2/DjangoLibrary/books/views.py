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
            return redirect('file_list')
        else:
            error = 'Форма была заполнена некорректно'

    form = NoModeratedBooksModelForm()
    context = {'form': form,
               'error': error
               }
    return render(request, 'books/addbook.html', context)

def file_list(request):
    files = NoModeratedBooksModel.objects.all()
    return render(request, 'books/file_list.html', {'files': files})

def file_detail(request, pk):
    file_instance = NoModeratedBooksModel.objects.get(pk=pk)
    with file_instance.txt.open('r') as f:
        content = f.read()
    return render(request, 'books/file_detail.html', {'content': content})
