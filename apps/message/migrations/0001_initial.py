# Generated by Django 2.1 on 2019-06-05 08:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.CharField(max_length=500, verbose_name='留言内容')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/message/', verbose_name='图片')),
                ('users', models.ManyToManyField(related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='留言相关人员')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
                'db_table': 'message',
            },
        ),
    ]
