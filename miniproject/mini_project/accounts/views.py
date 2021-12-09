from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth.decorators import login_required


def user_login(request):
    next = request.GET.get('next')
    print(next)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                if next:
                    return redirect(next)
                return redirect('blog:all_posts')
            else:
                messages.error(request, 'wrong username or password', 'warning')
                return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            login(request, user)
            messages.success(request, 'you registered successfully, now login', 'success')
            return redirect('blog:all_posts')
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})


@login_required(login_url='accounts:user_login')
def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('blog:all_posts')


@login_required(login_url='accounts:user_login')
def user_dashboard(request, id):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user=user)
    self_dash = False
    if request.user.id == id:
        self_dash = True
    return render(request, 'accounts/dashboard.html', {'user': user, 'posts': posts, 'self_dash': self_dash})








