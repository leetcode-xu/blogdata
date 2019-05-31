from django.db import models
from account.models import User
from django.utils.deconstruct import deconstructible
# Create your models here.


# class Voke(models.Model):
#     user = models.ForeignKey(User)
#
#     class Meta:
#         verbose_name = '博客类型'
#         verbose_name_plural = verbose_name
#         db_table = 'blogtype'

@deconstructible
class BlogType(models.Model):
    type = models.CharField(max_length=20, verbose_name='类型')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = '博客类型'
        verbose_name_plural = verbose_name
        db_table = 'blogtype'


class Topic(models.Model):
    tags = [(1, '美词佳句'),(2, '经典说说'), (3, '搞笑说说'), (4, '爱情说说'), (5, '伤感说说')]
    tag = models.IntegerField(choices=tags, default=1, verbose_name='标签')
    title = models.CharField(max_length=200, verbose_name='标题')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    read_num = models.IntegerField(verbose_name='阅读量', default=0)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/images/', null=True, verbose_name='图片')
    blog_type = models.ForeignKey(BlogType, default=2, related_name='topics', verbose_name='博客类型', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=2, related_name='topics', verbose_name='发表用户', on_delete=models.CASCADE)
    aixin = models.IntegerField(default=0)

    class Meta:
        verbose_name = '话题'
        verbose_name_plural = verbose_name
        db_table = 'topic'


class Reply(models.Model):
    topic = models.ForeignKey(Topic, related_name='topics', verbose_name='被回复的话题', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='回复内容')
    time = models.DateTimeField(auto_now_add=True, verbose_name='回复时间')
    users = models.ManyToManyField(User, related_name='replys', verbose_name='用户组')

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = verbose_name
        db_table = 'reply'