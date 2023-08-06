from django.db import models
from django.contrib.auth.models import User

""" TODO:
    [ ] fix to current timezone
    [ ] tweak error message when going over character limit
    [X] add likes
    [X] add RTs
    [ ] add comments
"""

class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=140, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    likes = models.ManyToManyField(User, related_name='tweet_likes', blank=True)

    def likes_count(self):
        return self.likes.count()
    
    def is_retweet(self):
        return self.parent != None
    
    def retweet_count(self):
        return Tweet.objects.filter(parent=self).count()
    
    def retweeters(self):
        qs = Tweet.objects.filter(parent=self)
        user_obj_list = []
        for obj in qs:
            user_obj_list.append(obj.user)
        return user_obj_list

    def __str__(self):
        return (f"{self.user}: "
                f"{self.body} "
                f"[{self.created_at: %Y-%m-%d %H:%M}]" 
                )
