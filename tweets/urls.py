from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('like_tweet/<int:pk>', views.like_tweet, name='like_tweet'),
    path('status/<int:pk>', views.show_tweet, name='show_tweet'),
    path('delete_tweet/<int:pk>', views.delete_tweet, name='delete_tweet'),
    path('retweet/<int:pk>', views.retweet, name='retweet'),
    path('bookmark/<int:pk>', views.bookmark, name='bookmark'),
    path('bookmarks', views.bookmarks_list, name='bookmarks_list'),

]
