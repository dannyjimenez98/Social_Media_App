# Generated by Django 4.2.3 on 2023-08-05 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_tweet_retweets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='retweets',
        ),
    ]
