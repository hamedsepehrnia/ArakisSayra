from django.db import models
import re

from mptt.models import MPTTModel, TreeForeignKey

from slugify import slugify


class Category(MPTTModel):
    name = models.CharField(max_length=100, blank =True, null=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name_plural = "دسته‌بندی‌ها"

    # def __str__(self):
    #     # full_path = [self.name]
    #     # parent = self.parent
    #     # while parent is not None:
    #     #     full_path.append(parent.name)
    #     #     parent = parent.parent
    #     # return ' > '.join(full_path[::-1])
    #     return self.name
    def __str__(self):
        return self.name

    def get_full_slug(self):
        """Return the full slug path from root to this category"""
        ancestors = []
        current = self
        while current:
            if current.slug:  # Only add if slug exists
                ancestors.insert(0, current.slug)
            current = current.parent
        return '/'.join(ancestors) if ancestors else self.slug or ''

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            ModelClass = self.__class__

            while ModelClass.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField("عنوان", max_length=255, null=True, blank=True)
    slug = models.SlugField("اسلاگ", unique=True, blank=True, null=True, allow_unicode=True)
    short_description = models.TextField("توضیح کوتاه", blank=True, null=True)
    description = models.TextField("توضیحات کامل", blank=True, null=True)
    size = models.PositiveSmallIntegerField("اندازه", blank=True, null=True)
    container_type = models.CharField("نوع بسته‌بندی", max_length=100, blank=True, null=True)
    attributes = models.CharField("ویژگی‌ها", max_length=255, blank=True, null=True)
    image = models.ImageField('تصویر', upload_to='products', blank=True, null=True)
    category = models.ForeignKey(
        "Category",
        verbose_name="دسته‌بندی",
        on_delete=models.CASCADE,
        related_name="products"
    )

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def get_full_slug(self):
        ancestors = []
        current = self.category
        while current:
            ancestors.insert(0, current.slug)
            current = current.parent
        return '/'.join(ancestors)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            ModelClass = self.__class__

            while ModelClass.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)
