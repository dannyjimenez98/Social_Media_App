# Generated by Django 4.2.3 on 2023-07-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_rename_post_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=1),
        ),
    ]
