# Generated by Django 4.2.3 on 2023-07-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_alter_tweet_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=140),
        ),
    ]