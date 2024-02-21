from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name = 'Artist Image', null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        self.user = self.user.capitalize()
        return super().save(*args, **kwargs)

class Category(models.Model):
    cat_name = models.CharField(verbose_name = 'Category Name', max_length = 100)
    image = models.ImageField(verbose_name = 'Category Image', null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        return self.cat_name

    def save(self, *args, **kwargs):
        self.cat_name = self.cat_name.capitalize()
        return super().save(*args, **kwargs)

class Products(models.Model):
    prod_name = models.CharField(verbose_name = 'Product Name', max_length = 100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name = 'Category Image', null=True, blank=True, upload_to='uploads/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(verbose_name = 'Description', blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,) 

    
    def __str__(self):
        return self.prod_name

    def save(self, *args, **kwargs):
        self.prod_name = self.prod_name.capitalize()
        self.slug = slugify(self.prod_name)
        return super().save(*args, **kwargs)

class News(models.Model):
    title = models.CharField(verbose_name = 'Post Title', max_length = 100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    article = models.TextField()
    image = models.ImageField(verbose_name = 'News Image', null=True, blank=True, upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True,) 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.capitalize()
        return super().save(*args, **kwargs)

