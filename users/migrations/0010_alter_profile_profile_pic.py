# Generated by Django 4.2.3 on 2023-08-03 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_follow_follow_user_alter_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default_profile_picture.jpeg', upload_to='media/'),
        ),
    ]
