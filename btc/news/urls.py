from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='news-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comment', CommentCreateView.as_view(), name='comment-post'),
    path('post/<int:post_id>/comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('post/<int:post_id>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:post_id>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('about/', views.about, name='news-about'),
]