from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.profile, name='profile'),
    path('<int:pk>/followers', views.get_followers, name='followers'),
    path('<int:pk>/following', views.get_following, name='following'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
]