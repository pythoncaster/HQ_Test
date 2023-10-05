from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    duration_in_sec = models.PositiveIntegerField(default=1)
    link = models.URLField(blank=True)
    time_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ManyToManyField(Lesson, blank=True)

    def __str__(self):
        return self.title


class ProductAccess(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Access {self.user} to {self.product}'
