from django.db import models
from account.models import User
# Create your models here.


class Message(models.Model):
    users = models.ManyToManyField(User, related_name='messages', verbose_name='留言相关人员')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    content = models.CharField(max_length=500, verbose_name='留言内容')
    image = models.ImageField(null=True, blank=True, verbose_name='图片', upload_to='static/images/message/')
    root = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='root_comment', verbose_name='被回复留言的id')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='parent_comment', verbose_name='被回复留言的id')

    class Meta:
        db_table = 'message'
        verbose_name = '留言'
        verbose_name_plural = verbose_name