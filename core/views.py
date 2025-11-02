from django.shortcuts import render, redirect
from .forms import MessageForm
from django.utils import translation
from blog.models import Post, News, Category as BlogCategory
from products.models import Product, Category as ProductCategory
from .models import Banner, SiteInfo


def index(request):
    # Get latest 4 blog posts
    latest_posts = Post.objects.all().order_by('-created_date')[:4]
    # Get banners
    banners = Banner.objects.all().order_by('-created_date')
    # Get latest products (based on ID)
    latest_products = Product.objects.all().order_by('-id')[:4]
    # Get site information
    site_info = SiteInfo.objects.first()
    about_text = site_info.about_text if site_info else ''
    picture = site_info.about_image if site_info else None
    
    return render(request, 'core/index.html', {
        'latest_posts': latest_posts,
        'banners': banners,
        'latest_products': latest_products,
        'about_text': about_text,
        'picture': picture,
    })


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