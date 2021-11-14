from django.shortcuts import render
from .models import Category

def sayCategory(request):
    return render(request, 'category.html')

def All_Category(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'categories.html', context)