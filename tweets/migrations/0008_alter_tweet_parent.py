# Generated by Django 4.2.3 on 2023-08-05 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_alter_tweet_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tweets.tweet'),
        ),
    ]
