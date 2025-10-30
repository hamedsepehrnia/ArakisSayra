from calendar import month

import jdatetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from oauth2client.transport import request
from slugify import slugify
from django.db import models
from django_jalali.db import models as jmodels
from core.image_optimizer import optimize_blog_image

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='دسته بندی')
    slug = models.SlugField('اسلاگ', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'دسته‌بندی‌ها'
        verbose_name = 'دسته بندی'
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    category = models.ManyToManyField(Category, related_name="posts", blank=True, verbose_name="دسته بندی")
    title = models.CharField("عنوان", max_length=100)
    slug = models.SlugField("نامک", unique=True, blank=True)
    image = models.ImageField(
        "تصویر شاخص", 
        upload_to="blog/", 
        null=True, 
        blank=True,
        help_text='📐 سایز بهینه: 900×585 پیکسل | نسبت: 3:2 (Landscape) | حداکثر حجم: 300KB'
    )
    content = models.TextField("محتوا")
    created_date = jmodels.jDateField("تاریخ ایجاد", auto_now_add=True, null=True, blank=True)
    created_time = models.TimeField("ساعت ایجاد", auto_now_add=True, null=True, blank=True)

    author = models.ForeignKey(
        User,
        verbose_name="نویسنده",
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True
    )

    def month_name(self):
        month = self.created_date.strftime('%B').lower()
        match month:
            case "farvardin":
                return "فروردین"
            case "ordibehesht":
                return "اردیبهشت"
            case "khordad":
                return "خرداد"
            case "tir":
                return "تیر"
            case "mordad":
                return "مرداد"
            case "shahrivar":
                return "شهریور"
            case "mehr":
                return "مهر"
            case "aban":
                return "آبان"
            case "azar":
                return "آذر"
            case "dey":
                return "دی"
            case "bahman":
                return "بهمن"
            case "esfand":
                return "اسفند"
            case _:
                return month

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # بهینه‌سازی تصویر پست قبل از ذخیره
        if self.image:
            self.image = optimize_blog_image(self.image)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = jmodels.jDateField("تاریخ ایجاد", auto_now_add=True, null=True, blank=True)
    created_time = models.TimeField("ساعت ایجاد", auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='نامک', null= True, blank=True)
    image = models.ImageField(
        upload_to="blog/news", 
        null=True, 
        blank=True,
        verbose_name='تصویر خبر',
        help_text='📐 سایز بهینه: 900×585 پیکسل | نسبت: 3:2 (Landscape) | حداکثر حجم: 300KB'
    )
    class Meta:
        verbose_name_plural = 'اخبار'
        verbose_name = 'خبر'
    def __str__(self):
        return self.title    
    def month_name(self):
        month = self.created_date.strftime('%B').lower()
        match month:
            case "farvardin":
                return "فروردین"
            case "ordibehesht":
                return "اردیبهشت"
            case "khordad":
                return "خرداد"
            case "tir":
                return "تیر"
            case "mordad":
                return "مرداد"
            case "shahrivar":
                return "شهریور"
            case "mehr":
                return "مهر"
            case "aban":
                return "آبان"
            case "azar":
                return "آذر"
            case "dey":
                return "دی"
            case "bahman":
                return "بهمن"
            case "esfand":
                return "اسفند"
            case _:
                return month
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # بهینه‌سازی تصویر خبر قبل از ذخیره
        if self.image:
            self.image = optimize_blog_image(self.image)
        
        super().save(*args, **kwargs)