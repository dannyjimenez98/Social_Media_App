# Generated by Django 4.2.3 on 2023-08-02 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_following_delete_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_followed', models.DateTimeField(auto_now_add=True)),
                ('follow_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_user', to='users.profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='users.profile')),
            ],
        ),
    ]
