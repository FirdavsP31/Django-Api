from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/')
    price = models.PositiveBigIntegerField()
    published = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    author_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.author_name

class Category(models.Model):
    category_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name

