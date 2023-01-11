from django.urls import path
from . views import PostView,PostListView


urlpatterns = [
    path('post/',PostView.as_view(),name='posts'),
    path('post/<int:post_pk>/',PostView.as_view(),name='posts'),
    path('postlist/',PostListView.as_view(),name='postlist'),


]

