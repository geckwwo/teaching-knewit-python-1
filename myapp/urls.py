from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user/<str:username>', views.user_profile)
]