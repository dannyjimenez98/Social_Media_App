from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, EditProfileForm
from .models import Profile, Follow
from tweets.models import Tweet

def profile(request, pk):
    if request.user.is_authenticated:
        # requested profile user and their tweets
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk).order_by('-created_at')

        user = Profile.objects.get(user_id=request.user.id) # currently logged in user
        isFollowing = user.following.filter(follow_user=profile).exists() # if user follows requested profile
        
        # handle follow/unfollow
        if request.method == 'POST':
            if isFollowing:
                Follow.objects.filter(user=user, follow_user=profile).delete()
            else:
                Follow.objects.create(user=user, follow_user=profile)
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'profile.html', {'profile':profile, 'tweets': tweets, 'isFollowing': isFollowing})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')

def get_followers(request, pk):
        profile = Profile.objects.get(user_id=pk).user.id

        # returns queryset of profile's follower relationships
        followers = Follow.objects.filter(follow_user=profile)
        return render(request, 'followers.html', {'profile':profile, 'followers':followers})


def get_following(request, pk):
    profile = Profile.objects.get(user_id=pk).user.id

    # returns queryset of profile's following relationships
    follows = Follow.objects.filter(user=profile)
    return render(request, 'following.html', {'profile':profile, 'follows':follows})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('edit_profile')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# create profile after new user is saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Error logging in...Try Again")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def logout_view(request):
    logout(request)
    return redirect('home')

def edit_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        
        # get forms
        profile_form = EditProfileForm(request.POST or None, request.FILES or None, instance=profile_user)

        if profile_form.is_valid():
            profile_form.save()

            login(request, current_user)
            messages.success(request, ("Your profile has been updated"))
            return redirect('home')
        
        if (request.META['HTTP_REFERER'] == '/users/signup'):
            header = 'Finish Profile'
        else:
            header = 'Edit Profile'
        return render(request, 'edit_profile.html', {'profile_form':profile_form, 'header':header})
    else:
        messages.success(request, ("You must be logged in to view that page"))
        return redirect('home')

def search(request):
    # if request made with htmx
    if request.htmx:
        search = request.GET.get('query')
        if search:
            # filter profile results based on username
            profile_results = [p for p in Profile.objects.all() if search in p.user.username]
        else:
            profile_results = Profile.objects.none()

        return render(request, 'search_results.html', {'profile_results': profile_results})
    
    return render(request, 'search.html')

def follow_suggestions(request):
    if request.user.is_authenticated:
        if request.htmx:
            user = Profile.objects.get(user=request.user)
            # get profiles user does not follow yet
            suggested_profiles=[p for p in Profile.objects.all() if p not in Follow.objects.filter(user=user) and p != user]
            return render(request, 'follow_suggestions.html', {'suggested_profiles': suggested_profiles})
        else:
            return render(request, 'sidebar.html')
    else:
        return redirect('home')
