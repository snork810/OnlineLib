from .models import NoModeratedBooksModel
from django.forms import ModelForm, TextInput, NumberInput, FileInput, Textarea


class NoModeratedBooksModelForm(ModelForm):
    class Meta:
        model = NoModeratedBooksModel
        fields = ['title', 'summary', 'pages', 'txt', 'author', 'category']
        widgets = {
            'title': TextInput(attrs={
                    'class': "form-control",
                    'placeholder': "Название книги"
            }),
            'summary': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Аннотация"
            }),
            'author': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Автор"
            }),
            'category': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Жанр"
            }),
            'pages': NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Количество страниц"
            }),
            'txt': FileInput(attrs={
                'class': "form-control",
                'placeholder': "Загрузка файла"
            }),
        }