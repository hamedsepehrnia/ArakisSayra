from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post, News, Category as BlogCategory
from products.models import Product, Category as ProductCategory
from django.utils import timezone


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['index', 'about', 'contact']

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created_date

    def location(self, obj):
        return f'/blog/{obj.slug}/'


class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created_date

    def location(self, obj):
        return f'/blog/news/{obj.slug}'


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return f'/products/{obj.slug}/'


class ProductCategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return ProductCategory.objects.all()

    def location(self, obj):
        return f'/products/category/{obj.get_full_slug()}/'


class BlogCategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return BlogCategory.objects.all()

    def location(self, obj):
        return f'/blog/category/{obj.name}/' 