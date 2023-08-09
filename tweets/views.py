from django.shortcuts import render, redirect
from .models import Tweet
from users.models import Profile, Follow
from .forms import TweetForm
from django.contrib import messages
from django.db.models import Q

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
            
        # tweets from followed users to be displayed on homepage
        user = Profile.objects.get(user=request.user)
        followed_users = []
        for followed_user in Follow.objects.filter(user=user):
            followed_users.append(followed_user.follow_user.user)
        
        # TODO: include replies but with "User replied to" tag above
        tweets = Tweet.objects.filter(Q(user__in=followed_users)|Q(user=request.user) & Q(reply_to=None)).order_by('-created_at')
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
        form = TweetForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                reply = form.save(commit=False)
                reply.user = request.user
                reply.reply_to = Tweet.objects.get(id=pk)
                reply.save()
                return redirect(request.META.get('HTTP_REFERER'))
        replies = Tweet.objects.filter(reply_to=tweet)
        return render(request, 'show_tweet.html', {'tweet':tweet, 'form': form, 'replies': replies})
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

# handles bookmarking a tweet
def bookmark(request, pk):
    if request.user.is_authenticated:
        tweet = Tweet.objects.get(id=pk)
        if tweet.bookmarks.filter(id=request.user.id):
            tweet.bookmarks.remove(request.user)
        else:
            tweet.bookmarks.add(request.user)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, ("Your must be logged in to view that page"))
        return redirect('home')
    
def bookmarks_list(request):
    if request.user.is_authenticated:
        # get tweets that were bookmarked by the  user
        bookmarked_tweets = Tweet.objects.filter(bookmarks=request.user).order_by('-created_at')
        return render(request, 'bookmarks.html', {'bookmarked_tweets': bookmarked_tweets})
    else:
        messages.success(request, ("Your must be logged in to view that page"))
        return redirect('home')