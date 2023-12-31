# Generated by Django 4.2.3 on 2023-08-03 23:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_alter_tweet_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
