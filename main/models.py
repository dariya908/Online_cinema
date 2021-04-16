from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)

    def __str__(self):
        return self.name


class Rating(models.Model):
    '''Рэйтинг'''

    movie=models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True,related_name ='rating')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ratings=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    rating = models.IntegerField(choices=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ), max_length=2)

    date_create = models.DateField(auto_now_add=True)

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    """Фильм"""
    trailer = models.FileField(blank=True, null=True, verbose_name='Трейлер')
    video=models.FileField(blank=True,null=True,verbose_name='Фильм')
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    avg_rate=models.FloatField(default=0)


    def __str__(self):
        return self.title

class Comment(models.Model):

    movie=models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True,related_name ='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)

