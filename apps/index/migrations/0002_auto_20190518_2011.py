# Generated by Django 2.1 on 2019-05-18 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='index.BlogType', verbose_name='博客类型'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
    ]
