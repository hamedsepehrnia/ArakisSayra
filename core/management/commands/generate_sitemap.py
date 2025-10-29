from django.core.management.base import BaseCommand
from django.contrib.sitemaps import get_sitemap_urls
from django.urls import reverse
from core.sitemap import (
    StaticViewSitemap, PostSitemap, NewsSitemap, 
    ProductSitemap, ProductCategorySitemap, BlogCategorySitemap
)


class Command(BaseCommand):
    help = 'Generate and test sitemap URLs'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Generating sitemap URLs...'))
        
        # Test static sitemap
        static_sitemap = StaticViewSitemap()
        self.stdout.write('\nStatic Pages:')
        for item in static_sitemap.items():
            url = static_sitemap.location(item)
            self.stdout.write(f'  - {url}')
        
        # Test blog sitemap
        try:
            post_sitemap = PostSitemap()
            posts = post_sitemap.items()
            self.stdout.write(f'\nBlog Posts: {posts.count()} posts')
            for post in posts[:5]:  # Show first 5
                url = post_sitemap.location(post)
                self.stdout.write(f'  - {url}')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Blog posts error: {e}'))
        
        # Test news sitemap
        try:
            news_sitemap = NewsSitemap()
            news_items = news_sitemap.items()
            self.stdout.write(f'\nNews: {news_items.count()} news items')
            for news in news_items[:5]:  # Show first 5
                url = news_sitemap.location(news)
                self.stdout.write(f'  - {url}')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'News error: {e}'))
        
        # Test products sitemap
        try:
            product_sitemap = ProductSitemap()
            products = product_sitemap.items()
            self.stdout.write(f'\nProducts: {products.count()} products')
            for product in products[:5]:  # Show first 5
                url = product_sitemap.location(product)
                self.stdout.write(f'  - {url}')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Products error: {e}'))
        
        # Test product categories sitemap
        try:
            category_sitemap = ProductCategorySitemap()
            categories = category_sitemap.items()
            self.stdout.write(f'\nProduct Categories: {categories.count()} categories')
            for category in categories[:5]:  # Show first 5
                url = category_sitemap.location(category)
                self.stdout.write(f'  - {url}')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Product categories error: {e}'))
        
        # Test blog categories sitemap
        try:
            blog_category_sitemap = BlogCategorySitemap()
            blog_categories = blog_category_sitemap.items()
            self.stdout.write(f'\nBlog Categories: {blog_categories.count()} categories')
            for category in blog_categories[:5]:  # Show first 5
                url = blog_category_sitemap.location(category)
                self.stdout.write(f'  - {url}')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Blog categories error: {e}'))
        
        self.stdout.write(self.style.SUCCESS('\nSitemap generation completed!'))
        self.stdout.write('You can access the sitemap at: /sitemap.xml')
        self.stdout.write('HTML sitemap at: /sitemap/') 