from django.urls import path
from .views import TweetList, TweetDetail

urlpatterns = [
    path('', TweetList.as_view()),
    path('<int:pk>', TweetDetail.as_view()),
]