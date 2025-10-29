from django.urls import path

from products import views

urlpatterns = [
    path('search/', views.product_search, name='product_search'),
    path('category/<path:full_path>/', views.category_products_by_path, name='products_category'),
    path('<slug:slug>/', views.single_product, name='product_detail'),
    path('', views.all_products, name='all_products'),

]
