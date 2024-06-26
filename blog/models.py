from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    permalink = models.SlugField(max_length=128, unique=True, blank=True)

    def get_absolute_url(self):
        return "blog-detail", [self.permalink, ]

    def save(self, *args, **kwargs):
        if not self.permalink:
            self.permalink = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.title