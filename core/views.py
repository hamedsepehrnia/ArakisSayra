from django.shortcuts import render, redirect
from .forms import MessageForm
from django.utils import translation
from blog.models import Post, News, Category as BlogCategory
from products.models import Product, Category as ProductCategory
from .models import Banner, SiteInfo


def index(request):
    # دریافت آخرین 4 پست بلاگ
    latest_posts = Post.objects.all().order_by('-created_date')[:4]
    banners = Banner.objects.all().order_by('-created_date')
    return render(request, 'core/index.html', {'latest_posts': latest_posts, 'banners': banners})


def about(request):
    site_info = SiteInfo.objects.first()
    picture = site_info.about_image
    context = {
        'picture': picture,
    }
    return render(request, 'core/about-us.html', context)


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MessageForm()
    return render(request, 'core/contact-us.html', {'form': form})


def sitemap_view(request):
    """HTML Sitemap view"""
    context = {
        'posts': Post.objects.all().order_by('-created_date'),
        'news': News.objects.all().order_by('-created_date'),
        'products': Product.objects.all(),
        'product_categories': ProductCategory.objects.all(),
        'blog_categories': BlogCategory.objects.all(),
    }
    return render(request, 'core/sitemap.html', context)