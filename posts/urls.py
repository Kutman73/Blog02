from django.urls import path
from posts.views import *

urlpatterns = [
    path('posts/', posts_view),
    path('posts/<int:id>/', detail_post_view),
    path('hashtags/', hashtags_view),
    path('posts/create/', post_create_view)
]
