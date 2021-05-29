from django.contrib.auth import get_user_model
from django.db import models

CHOICES = (("private", "Приватный"),
           ("public", "Публичный")
)


class Photo(models.Model):
    photo = models.ImageField(upload_to='product_pic', null=False, blank=False, verbose_name='Картинка')
    signature = models.CharField(max_length=200, null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        related_name='photos'
    )
    album = models.ForeignKey('gallery.Album', on_delete=models.CASCADE, null=True, related_name='photos')
    favourites = models.ManyToManyField(get_user_model(), related_name='fav_photos', db_table='photo_users', null=True, blank=True)
    type = models.CharField(max_length=200, choices=CHOICES, verbose_name='тип')


class Album(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        related_name='albums'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=200, choices=CHOICES, verbose_name='тип')
