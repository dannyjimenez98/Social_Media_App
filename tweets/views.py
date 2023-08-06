from django.shortcuts import render, redirect
from .models import Tweet
from users.models import Profile
from .forms import TweetForm
from django.contrib import messages

# handles display of tweets on home feed and create/publish a tweet
def home_view(request):
    if request.user.is_authenticated:
        # tweet creation form
        form = TweetForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('home')
        # tweets to be displayed on homepage
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'tweets': tweets, 'form': form})
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'tweets': tweets})

# handles liking and unliking of tweets by user
def like_tweet(request, pk):
    if request.user.is_authenticated:
        tweet = Tweet.objects.get(id=pk)
        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user)
        else:
            tweet.likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, ("Your must be logged in to view that page"))
        return redirect('home')

def retweet(request, pk):
    if request.user.is_authenticated:
        user = request.user
        tweet = Tweet.objects.get(id=pk)

        # if its a RT of a post
        if tweet.is_retweet():
            
            # user RTed
            if user in tweet.parent.retweeters():
                Tweet.objects.get(parent=tweet.parent, user=user).delete() # delete user's RT of original tweet
                return redirect(request.META.get('HTTP_REFERER'))
            
            # if user did not RT, create RT of original tweet
            else:
                Tweet.objects.create(parent=tweet.parent, user=user)
        
        # original post
        else:
            # user RTed
            if user in tweet.retweeters():
                Tweet.objects.get(parent=tweet, user=user).delete() # delete user's RT of original tweet
                return redirect(request.META.get('HTTP_REFERER'))
            
            # if user did not RT, create RT of tweet
            else:
                Tweet.objects.create(parent=tweet, user=user)
        return redirect(request.META.get('HTTP_REFERER'))
    
    else:
        messages.success(request, ("Your must be logged in to view that page"))
        return redirect('home')

# handles clicking of tweet to show tweet in detail
def show_tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    if tweet:
        return render(request, 'show_tweet.html', {'tweet':tweet})
    else:
        messages.success(request, ("tweet does not exist"))
        return redirect('home')

def delete_tweet(request, pk):
    if request.user.is_authenticated:
        tweet = Tweet.objects.get(id=pk)
        if request.user.username == tweet.user.username:
            tweet.delete()
            messages.success(request, ("Tweet successfully deleted"))
            return redirect('home')
    else:
        messages.success(request, ("Log in to delete tweet"))
        return redirect(request.META.get('HTTP_REFERER'))
    
# def bookmark(request, pk):
    if request.user.is_authenticated:
        user = request.user
        tweet = Tweet.objects.get(id=pk)
        profile = Profile.objects.get(user_id=user.id)
        if tweet in profile.bookmarked_tweets.filter(id=tweet.id):
            profile.bookmarked_tweets.remove(tweet)
        else:
            profile.bookmarked_tweets.add(tweet)
    else:
        return redirect('home')