from django.shortcuts import render
from .models import Post, Category, Comment
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



def all_posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'all_posts': all_posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.filter(post__slug=slug)
    return render(request, 'blog/post.html', {'post': post, 'comment':comment})


def all_category(request):
    all_category = Category.objects.all()
    return render(request, 'blog/all_category.html', {'all_category': all_category})


def category_detail(request, id):
    category = Category.objects.get(id=id)
    post = category.post.all()
    return render(request, 'blog/category.html', {'category': category, 'post':post})


class ListPost(TemplateView):
    template_name = 'blog/list_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class DetailPost(DetailView): # blog/post_detail.html
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'myslug'


class ListCategory(ListView):
    template_name = 'blog/list_category.html'
    model = Category
    context_object_name = 'categories'


class DetailCategory(DetailView):
    model = Category





