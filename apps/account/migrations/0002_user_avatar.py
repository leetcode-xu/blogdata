# Generated by Django 2.1 on 2019-05-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/images/uploads/avatar/default.jpg', upload_to='static/images/uploads/avatar/'),
        ),
    ]
