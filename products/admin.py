from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from products.models import Product, Category

admin.site.register(Product)

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
