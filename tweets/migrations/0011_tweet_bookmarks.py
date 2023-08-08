# Generated by Django 4.2.3 on 2023-08-08 22:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0010_remove_tweet_retweets'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, related_name='tweet_bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
