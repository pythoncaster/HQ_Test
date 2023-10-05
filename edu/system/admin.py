from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_in_sec')


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')