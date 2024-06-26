from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request, category_id=None):
    if category_id:
        posts = Post.objects.filter(category_id=category_id).order_by('-created_at')
        selected_category = get_object_or_404(Category, pk=category_id)
    else:
        posts = Post.objects.all().order_by('-created_at')
        selected_category = None
    categories = Category.objects.all()
    return render(request, 'post_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': selected_category,
    })


def post_detail(request, permalink):
    post = get_object_or_404(Post, permalink=permalink)
    categories = Category.objects.all()
    return render(request, 'post_detail.html', {
        'post': post,
        'categories': categories,
    })
