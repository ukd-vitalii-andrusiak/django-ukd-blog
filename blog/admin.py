from django.contrib import admin
from .models import Post, Category, Image


class ImageInline(admin.TabularInline):
    model = Image


class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    prepopulated_fields = {'permalink': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Image)
