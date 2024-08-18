from django.db import models

# Create your models here.

class NoModeratedBooksModel(models.Model):
    title = models.CharField('Название', max_length=80)
    summary = models.TextField('Аннотация',max_length=10000)
    pages = models.IntegerField("Количество страниц")
    txt = models.FileField("Загрузите файл",upload_to='Texts/')
    author = models.CharField('Автор', max_length=50)
    category = models.CharField("Категория",max_length=80)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Не модерированное'