from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from news.models import Post
from django.contrib.auth.models import User
from news import models as news_models
from django.core.paginator import Paginator


def register(request):
    '''
    registers a user if they provided a valid form
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}'s account has been created! You are now able to log in")
            redirect_page = 'login'  # redirect_page = name for url pattern for the blog home page
            return redirect(redirect_page)
        else:
            messages.warning(request, 'Please, read the instructions to register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form': form})


@login_required
def profile(request):
    '''
    updates a user profile
    '''
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            username = u_form.cleaned_data.get('username')
            messages.success(request, f"{username}'s account has been updated!")

            redirect_page = 'profile'
            return redirect(redirect_page) 
    else:
        # populate the forms with the current information
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # https://docs.djangoproject.com/en/3.1/topics/pagination/
    user_posts = news_models.Post.objects.filter(author=request.user).order_by('-date_posted')
    paginator = Paginator(user_posts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'page_obj': page_obj
    }

    return render(request, 'users/profile.html', context=context)