from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
# login required decorator for Class-Based Views
from django.contrib.auth.mixins import LoginRequiredMixin
# only the author can edit their posts
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse


class PostListView(ListView):
    model = Post
    template_name = 'news/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7


class UserPostListView(ListView):
    '''
    just like PostListView but filtered
    to posts written by specific user
    '''
    model = Post
    template_name = 'news/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        '''
        CONVENTION NAME

        we want to get the user
            associated with that username
            that we are gonna get from the url

        if the user does not exist -> return 404
        '''
        user = get_object_or_404(User, 
                                username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # the template: blog/post_detail.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'image', 'content']

    def form_valid(self, form):
        '''
        CONVENTION NAME

        sets current logged in user as author for `form`
        '''
        form.instance.author = self.request.user
        return super().form_valid(form)


# LoginRequiredMixin, UserPassesTestMixin HAVE TO BE TO THE LEFT OF GENERIC VIEWS
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'image', 'content']

    def form_valid(self, form):
        '''
        CONVENTION NAME

        sets current logged in user as author for `form`
        '''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
        CONVENTION NAME

        UserPassesTestMixin runs `test_func` in order to check
            if a user passes a certain test

        In our case: allows editing iff you are the author of the post
        Returns `403 Forbidden` otherwise
        '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        '''
        In our case: allows deleting iff you are the author of the post
        Returns `403 Forbidden` otherwise
        '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_url = '/'  # the rule for success on DELETE


class CommentDetailView(DetailView):
    model = Comment


class CommentListView(ListView):
    model = Comment
    template_name = 'news/post_detail.html'
    context_object_name = 'comments'  # html object name: object.comments
    ordering = ['-date_posted']


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        '''
        CONVENTION NAME

        sets current logged in user as author for `form`
        '''
        form.instance.author = self.request.user
        post = get_object_or_404(Post, 
                                id=self.kwargs.get('post_id'))
        form.instance.post_id = post.pk
        return super().form_valid(form)

    def get_success_url(self, post_id=None):
        success_url = reverse('post-detail', kwargs={'pk': self.kwargs.get('post_id')})
        return success_url


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        '''
        CONVENTION NAME

        sets current logged in user as author for `form`
        '''
        form.instance.author = self.request.user
        print(self.request.__dict__)
        post = get_object_or_404(Post,
                                id=self.kwargs.get('post_id'))
        form.instance.post_id = post.pk
        return super().form_valid(form)

    def test_func(self):
        '''
        CONVENTION NAME

        UserPassesTestMixin runs `test_func` in order to check
            if a user passes a certain test

        In our case: allows editing iff you are the author of the post
        Returns `403 Forbidden` otherwise
        '''
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_success_url(self, post_id=None):
        success_url = reverse('post-detail', kwargs={'pk': self.kwargs.get('post_id')})
        return success_url


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    success_url = '/'  # the rule for success on DELETE


def about(request):
    return render(request, 'news/about.html',
                context={'title': 'About us'})