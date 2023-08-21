from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=140, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    likes = models.ManyToManyField(User, related_name='tweet_likes', blank=True)
    bookmarks = models.ManyToManyField(User, related_name='tweet_bookmarks', blank=True)
    reply_to = models.ForeignKey("self", related_name='replied_to', null=True, blank=True, on_delete=models.CASCADE) 
    
    def likes_count(self):
        return self.likes.count()
    
    def is_retweet(self):
        return self.parent != None
    
    def retweet_count(self):
        return Tweet.objects.filter(parent=self).count()
    
    def retweeters(self):
        '''
        Returns list of users that retweeted this tweet
        '''
        qs = Tweet.objects.filter(parent=self)
        user_obj_list = []
        for obj in qs:
            user_obj_list.append(obj.user)
        return user_obj_list

    def bookmarks_count(self):
        return self.bookmarks.count()
    
    def is_reply(self):
        return self.reply_to != None
    
    def replies_count(self):
        return Tweet.objects.filter(reply_to=self).count()

    def __str__(self):
        return (f"{self.user}: "
                f"{self.body} "
                f"[{self.created_at: %Y-%m-%d %H:%M}]" 
                )
