"""
URL configuration for ArakisSayra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemap import (
    StaticViewSitemap, PostSitemap, NewsSitemap, 
    ProductSitemap, ProductCategorySitemap, BlogCategorySitemap
)

from django.conf.urls.i18n import i18n_patterns

# Sitemap configuration
sitemaps = {
    'static': StaticViewSitemap,
    'posts': PostSitemap,
    'news': NewsSitemap,
    'products': ProductSitemap,
    'product_categories': ProductCategorySitemap,
    'blog_categories': BlogCategorySitemap,
}

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),  # برای set_language
    path("admin/", admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += i18n_patterns(
    path("", include("core.urls")),
    path("blog/", include("blog.urls")),
    path("products/", include("products.urls")),
)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
