from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Category, Comment
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import AddPostForm, EditPostForm, AddCategoryForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required



def all_posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'all_posts': all_posts})


def post_detail(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.filter(post__slug=slug)
    return render(request, 'blog/post.html', {'post': post, 'comment': comment})


@login_required(login_url='accounts:user_login')
def add_post(request, id):
    if request.user.id == id:
        if request.method == 'POST':
            form = AddPostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.save()
                # new_post.slug = slugify(form.cleaned_data['title'])
                messages.success(request, 'your post submitted', 'success')
                return redirect('accounts:dashboard', id)
                # return redirect(f'/dashboard/{id}/')
        else:
            form = AddPostForm()
            return render(request, 'blog/add_post.html', {'form': form})
    else:
        return redirect('blog:all_posts')


@login_required(login_url='accounts:user_login')
def post_delete(request, id, post_id):
    if id == request.user.id:
        Post.objects.filter(id=post_id).delete()
        messages.success(request, 'your post deleted successfully', 'success')
        return redirect('accounts:dashboard', id)
    else:
        return redirect('blog:all_posts')


@login_required(login_url='accounts:user_login')
def post_edit(request, id, post_id):
    if request.user.id == id:
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                ep = form.save(commit=False)
                ep.save()
                messages.success(request, 'your post edited successfully', 'success')
                return redirect('accounts:dashboard', id)
        else:
            form = EditPostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('blog:all_posts')


def all_category(request):
    all_category = Category.objects.all()
    return render(request, 'blog/all_category.html', {'all_category': all_category})


def category_detail(request, id):
    category = Category.objects.get(id=id)
    post = category.post.all()
    return render(request, 'blog/category.html', {'category': category, 'post':post})


@login_required(login_url='accounts:user_login')
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            cate.save()
            messages.success(request, 'category submitted', 'success')
            return redirect('blog:all_category')
    else:
        form = AddCategoryForm()
        return render(request, 'blog/add_category.html', {'form': form})








