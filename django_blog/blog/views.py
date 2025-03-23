from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CommentForm
from django.db.models import Q


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "blog/login.html", {"error": "Invalid credentials"})
    return render(request, "blog/login.html")

@login_required
def update_profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "blog/update_profile.html", {"form": form})



from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]

# View a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Add a new comment
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post_id)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form, "post": post})

# Edit a comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect("post_detail", pk=comment.post.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "blog/edit_comment.html", {"form": form, "comment": comment})

# Delete a comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect("post_detail", pk=comment.post.id)
    if request.method == "POST":
        comment.delete()
        return redirect("post_detail", pk=comment.post.id)
    return render(request, "blog/delete_comment.html", {"comment": comment})


# Create a new comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["post_id"]
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_id"]})

# Update an existing comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})

# Delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})
    
def search_posts(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    return render(request, "blog/search_results.html", {"posts": posts, "query": query})

def posts_by_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, "blog/posts_by_tag.html", {"posts": posts, "tag": tag})

from django.views.generic import ListView
from .models import Post, Tag

class PostByTagListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        return Post.objects.filter(tags__slug=tag_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("tag_slug")
        return context