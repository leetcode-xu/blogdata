# Generated by Django 2.1 on 2019-05-28 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190523_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='index.Topic', verbose_name='被回复的话题'),
        ),
    ]
