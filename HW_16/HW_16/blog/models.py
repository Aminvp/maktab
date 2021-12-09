from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def unique_slugify(self, slug):
        model = self.__class__
        unique_slug = slug
        while model.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + str(random.randint(0, 12000))
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.unique_slugify(self, self.slug)
        super().save(*args, **kwargs)


class Comment(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=120)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category_detail', args=[self.id])
