from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Post
from django.contrib.auth.models import User
import time

# Create your views here.
def home(request):
    return render(request, "home.html")

def user_profile(request, username):
    users = User.objects.all().filter(username=username)
    if len(users) == 0:
        return render(request, 'user_not_found.html')
    
    user = users[0]

    posts = Post.objects.all().filter(user__username=username)
    
    return render(request, 'user_profile.html', {
        "posts": posts,
        "tag": username,
        "name": user.first_name,
        "id": user.pk,
        "date_joined": user.date_joined
    })