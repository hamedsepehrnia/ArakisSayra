from django.db import models
from products.models import Product


class SiteInfo(models.Model):
    phone_number1 = models.CharField("شماره تماس ۱", max_length=20)
    phone_number2 = models.CharField("شماره تماس ۲", max_length=20)
    phone_number3 = models.CharField("شماره تماس ۳", max_length=20)
    address = models.TextField("آدرس", max_length=255, null=True, blank=True)
    email = models.EmailField("ایمیل", null=True, blank=True)
    about_text = models.TextField("متن درباره ما", null=True, blank=True)
    about_image = models.ImageField(
        'تصویر درباره ما', 
        upload_to='about/', 
        null=True, 
        blank=True,
        help_text='📐 سایز بهینه: 800×600 پیکسل | نسبت: 4:3 | حداکثر حجم: 300KB'
    )
    work_hour1 = models.CharField(null=True, blank=True, max_length=255)
    work_hour2 = models.CharField(null=True, blank=True, max_length=255)
    work_hour3 = models.CharField(null=True, blank=True, max_length=255)
    instagram_page = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = 'اطلاعات وبسایت'
        verbose_name_plural = 'اطلاعات وبسایت'
    def __str__(self):
        return 'وبرایش اطلاعات وبسایت'
class Message(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    class Meta:
        verbose_name = 'پیام دریافت شده'
        verbose_name_plural = 'پیام های دریافت شده'
    def __str__(self):
        return self.subject + '-' + self.fullname
class Banner(models.Model):
    image = models.ImageField(
        upload_to='banners/', 
        verbose_name='تصویر بنر',
        help_text='📐 سایز بهینه: 1920×960 پیکسل | نسبت: 2:1 (Landscape) | حداکثر حجم: 500KB | عناصر مهم را در مرکز قرار دهید'
    )
    url = models.URLField(max_length=255, null=True, blank=True, verbose_name='لینک (اختیاری)')
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنر ها'