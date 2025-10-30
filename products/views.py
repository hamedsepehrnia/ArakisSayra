from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from mptt.templatetags.mptt_tags import cache_tree_children
from unicodedata import category

from products.models import Product, Category


# def products(request, category_choice=None):
#     if category_choice:
#         all_products = Product.objects.filter(category=category_choice)
#     else:
#         all_products = Product.objects.all()
#     paginator = Paginator(all_products, 10)  # تعداد آیتم در هر صفحه
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {'products': page_obj}
#     return render(request, 'products/products.html', context)
def single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    # Create breadcrumb for category path
    breadcrumb = []
    current_category = product.category
    while current_category:
        breadcrumb.insert(0, current_category)
        current_category = current_category.parent
    
    # Get related products from the same category
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'breadcrumb': breadcrumb,
        'related_products': related_products
    }
    return render(request, 'products/single-product.html', context)
# def shop(request):
#     return render(request, 'products/products_left.html')
def category_products_by_path(request, full_path):
    slug_list = full_path.strip('/').split('/')
    category = None
    categories = cache_tree_children(Category.objects.all())
    
    # Build breadcrumb
    breadcrumb = []
    for slug in slug_list:
        category = get_object_or_404(Category, slug=slug, parent=category)
        breadcrumb.append(category)

    products = Product.objects.filter(category__in=category.get_descendants(include_self=True))

    return render(request, 'products/products.html', {
        'category': category,
        'products': products,
        'categories': categories,
        'breadcrumb': breadcrumb
    })


def all_products(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 10)  # تعداد آیتم در هر صفحه
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'products/products.html', {
        'products': products,
        'breadcrumb': []  # Empty breadcrumb for main products page
    })
def product_search(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        results = Product.objects.filter(title__icontains=query)
    return render(request, 'products/search-result.html', {'query': query, 'results': results})