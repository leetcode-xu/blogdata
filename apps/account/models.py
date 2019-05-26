from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.deconstruct import deconstructible


@deconstructible
class User(AbstractUser):
    home_address = models.CharField(max_length=200, blank=True, null=True, verbose_name='个人博客')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话')
    avatar = models.ImageField(upload_to='static/images/uploads/avatar/', default='static/images/uploads/avatar/default.jpg')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 'user'
