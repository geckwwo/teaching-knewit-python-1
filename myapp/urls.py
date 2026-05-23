from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    path('', views.home),
    path('user/<str:username>', views.user_profile),
    *router.urls
]