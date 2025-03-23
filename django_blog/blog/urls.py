from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment, edit_comment, delete_comment,
    search_posts, posts_by_tag,
)

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/new/", PostCreateView.as_view(), name="post/new/"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/comments/new/", add_comment, name="add_comment"),
    path("comment/<int:comment_id>/edit/", edit_comment, name="edit_comment"),
    path("comment/<int:pk>/update/", delete_comment, name="delete_comment"),
       path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "comment/<int:pk>/update/",
        CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    path("search/", search_posts, name="search_posts"),
    path("tags/<str:tag>/", posts_by_tag, name="posts_by_tag"),
]