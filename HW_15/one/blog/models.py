from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedArticlesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')

class DraftedArticlesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='draft')

class Article(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=120, default='DEFAULT VALUE')
    slug = models.SlugField(max_length=120, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    objects = models.Manager()
    published = PublishedArticlesManager()
    drafted = DraftedArticlesManager()

    def __str__(self):
        return self.title
