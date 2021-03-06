# Generated by Django 2.1 on 2019-05-18 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
            ],
            options={
                'verbose_name': '博客类型',
                'verbose_name_plural': '博客类型',
                'db_table': 'blogtype',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='回复内容')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='回复时间')),
            ],
            options={
                'verbose_name': '回复',
                'verbose_name_plural': '回复',
                'db_table': 'Reply',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('read_num', models.IntegerField(verbose_name='阅读量')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('blog_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.BlogType', verbose_name='博客类型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL, verbose_name='发表用户')),
            ],
            options={
                'verbose_name': '话题',
                'verbose_name_plural': '话题',
                'db_table': 'topic',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Topic', verbose_name='被回复的话题'),
        ),
        migrations.AddField(
            model_name='reply',
            name='users',
            field=models.ManyToManyField(related_name='replys', to=settings.AUTH_USER_MODEL, verbose_name='用户组'),
        ),
    ]
