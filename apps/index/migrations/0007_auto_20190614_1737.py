# Generated by Django 2.1 on 2019-06-14 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0006_auto_20190531_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='users',
        ),
        migrations.AddField(
            model_name='reply',
            name='root',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chrild', to='index.Reply', verbose_name='根评论'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply1s', to=settings.AUTH_USER_MODEL, verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply2s', to=settings.AUTH_USER_MODEL, verbose_name='被@者'),
        ),
    ]
