from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class AvailableProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='available')

class UnavailableProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='unavailable')


class Product(models.Model):
    STATUS = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='available')
    objects = models.Manager()
    availables = AvailableProductManager()
    unavailables = UnavailableProductManager()



    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



