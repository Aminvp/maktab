from django.shortcuts import render
from .models import Article

def Published(request):
    published = Article.published.all()
    return render(request, 'published.html', {'published':published})



