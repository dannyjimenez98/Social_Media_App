# Generated by Django 4.2.3 on 2023-08-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_tweet_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]