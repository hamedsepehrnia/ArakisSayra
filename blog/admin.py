# admin.py
from django.contrib import admin
from .models import Post, Category, News
from django_jalali.admin.filters import JDateFieldListFilter

from django.contrib import admin
from .models import Post
from django_jalali.admin.filters import JDateFieldListFilter

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'created_time']
    list_filter = (
        ('created_date', JDateFieldListFilter),
    )
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from title
    fields = ('title', 'slug', 'image', 'content', 'author', 'category')  # Fields to show in admin form

    def save_model(self, request, obj, form, change):
        # If creating a new post (not editing), set the author to the current user
        if not change:  # change is False when creating a new object
            obj.author = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Category)
admin.site.register(News)
