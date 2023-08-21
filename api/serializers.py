from rest_framework import serializers
from tweets.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['user', 'likes', 'bookmarks']