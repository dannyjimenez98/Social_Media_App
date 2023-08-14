from django.db import models
from django.contrib.auth.models import User
from tweets.models import Tweet

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=10, default=" ")
    profile_pic = models.ImageField(default='default_profile_picture.jpeg', upload_to='media/')
    profile_bio = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.user.username
    
# model for join table between users following
class Follow(models.Model):
    user = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE, null=True)
    follow_user = models.ForeignKey(Profile, related_name="followers", on_delete=models.CASCADE, null=True)
    time_followed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.user.__str__()}" follows "{self.follow_user.__str__()}"'
