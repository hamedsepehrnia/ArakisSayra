# Arakis Sayra

**A Modern Bilingual E-commerce Platform Built with Django**

[فارسی](#فارسی) | [English](#english)

---

## English

### Overview

Arakis Sayra is a full-featured bilingual (Persian/English) e-commerce platform built with Django 5.2. The platform provides comprehensive product catalog management, blogging capabilities, and a modern responsive design suitable for corporate websites.

### Key Features

#### Multilingual Support
- Full Persian (Farsi) and English language support
- Django modeltranslation integration for seamless content translation
- Automatic URL routing based on language selection

#### Product Management
- Hierarchical category system using Django MPTT
- Product catalog with detailed specifications
- Automatic slug generation for SEO-friendly URLs
- Image optimization for fast loading
- Category-based product filtering

#### Content Management
- Blog posts with rich text content
- News section for company updates
- Category-based content organization
- Jalali calendar support for Persian dates
- Author management system

#### Image Optimization
- Automatic image resizing and compression
- Progressive JPEG encoding
- Configurable quality settings (85-88%)
- Optimized dimensions for different content types:
  - Banners: 1920×960 pixels
  - Products: 1000×1000 pixels
  - Blog/News: 900×585 pixels
  - About section: 800×600 pixels

#### Site Management
- Dynamic site information management
- Contact form with message storage
- Banner management system
- Customizable working hours and contact details
- Social media integration (Instagram)

### Technology Stack

- **Framework**: Django 5.2
- **Database**: SQLite (development) / MySQL (production support)
- **Languages**: Python 3.12
- **Frontend**: Bootstrap, jQuery
- **Image Processing**: Pillow
- **Translation**: django-modeltranslation
- **Calendar**: django-jalali (Jalali calendar support)
- **Category Trees**: django-mptt
- **Admin Interface**: Django Admin with Persian font support

### Installation

#### Prerequisites
- Python 3.12 or higher
- Virtual environment (recommended)
- Git

#### Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd ArakisSayra
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install gettext for translations:
```bash
# Ubuntu/Debian
sudo apt-get install gettext

# CentOS/RHEL
sudo yum install gettext
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Compile translations:
```bash
python manage.py compilemessages
```

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Create superuser:
```bash
python manage.py createsuperuser
```

9. Run development server:
```bash
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/`

### Project Structure

```
ArakisSayra/
├── ArakisSayra/          # Main project settings
├── blog/                 # Blog and news application
├── core/                 # Core functionality and site info
│   ├── image_optimizer.py
│   ├── management/commands/
│   └── templates/
├── products/             # Product catalog application
├── contex_processors/    # Custom context processors
├── static/               # Static files (CSS, JS, images)
├── media/                # User uploaded files
├── locale/               # Translation files
├── docs/                 # Documentation
│   ├── DEPLOYMENT_GUIDE.md
│   ├── IMAGE_OPTIMIZATION_GUIDE.md
│   └── TRANSLATION_GUIDE.md
└── requirements.txt
```

### Configuration

#### Database Configuration

**Development (SQLite):**
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

**Production (MySQL):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Static Files Configuration

**Development:**
```python
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

**Production:**
Update `STATIC_ROOT` and `MEDIA_ROOT` to your server paths.

### Management Commands

#### Generate Sample Data
```bash
python manage.py create_sample_data
```

#### Generate Sitemap
```bash
python manage.py generate_sitemap
```

#### Update Translations
```bash
./update_translations.sh
```

### Admin Panel

Access the admin panel at `/admin/` with your superuser credentials.

**Features:**
- Persian font support
- Jalali calendar integration
- Image upload with automatic optimization
- Category management with MPTT tree view
- Message inbox for contact form submissions

### Documentation

Detailed documentation is available in the `docs/` directory:

- **Deployment Guide**: Step-by-step instructions for deploying to production
- **Image Optimization Guide**: Information about automatic image optimization
- **Translation Guide**: How to manage and compile translations

### Endpoints

The project doesn't have a REST API by default, but all content is accessible through Django views.

### Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

You are free to:
- Share: copy and redistribute the material in any medium or format
- Adapt: remix, transform, and build upon the material

Under the following terms:
- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made
- NonCommercial: You may not use the material for commercial purposes

For more details, see the LICENSE file or visit: https://creativecommons.org/licenses/by-nc/4.0/

### Support

For issues and questions, please contact the development team.

---

## فارسی

### معرفی

آراکیس سایرا یک پلتفرم تجارت الکترونیک دوزبانه (فارسی/انگلیسی) کامل است که با Django 5.2 ساخته شده است. این پلتفرم مدیریت جامع کاتالوگ محصولات، امکانات وبلاگ و طراحی مدرن و ریسپانسیو مناسب برای وب‌سایت‌های شرکتی را فراهم می‌کند.

### ویژگی‌های کلیدی

#### پشتیبانی چندزبانه
- پشتیبانی کامل از زبان‌های فارسی و انگلیسی
- یکپارچه‌سازی django-modeltranslation برای ترجمه یکپارچه محتوا
- مسیریابی خودکار URL بر اساس انتخاب زبان

#### مدیریت محصولات
- سیستم دسته‌بندی سلسله مراتبی با استفاده از Django MPTT
- کاتالوگ محصول با مشخصات تفصیلی
- تولید خودکار اسلاگ برای URLهای سئو شده
- بهینه‌سازی تصویر برای بارگذاری سریع
- فیلتر محصولات بر اساس دسته‌بندی

#### مدیریت محتوا
- پست‌های وبلاگ با محتوای متنی غنی
- بخش اخبار برای به‌روزرسانی‌های شرکت
- سازماندهی محتوا بر اساس دسته‌بندی
- پشتیبانی از تقویم جلالی برای تاریخ‌های شمسی
- سیستم مدیریت نویسندگان

#### بهینه‌سازی تصاویر
- تغییر اندازه و فشرده‌سازی خودکار تصاویر
- کدگذاری Progressive JPEG
- تنظیمات کیفیت قابل تنظیم (85-88%)
- ابعاد بهینه شده برای انواع مختلف محتوا:
  - بنرها: 1920×960 پیکسل
  - محصولات: 1000×1000 پیکسل
  - بلاگ/اخبار: 900×585 پیکسل
  - بخش درباره ما: 800×600 پیکسل

#### مدیریت سایت
- مدیریت پویای اطلاعات سایت
- فرم تماس با ذخیره‌سازی پیام
- سیستم مدیریت بنر
- ساعات کاری و جزئیات تماس قابل تنظیم
- یکپارچه‌سازی شبکه‌های اجتماعی (اینستاگرام)

### پشته فناوری

- **فریمورک**: Django 5.2
- **پایگاه داده**: SQLite (توسعه) / MySQL (پشتیبانی تولید)
- **زبان‌ها**: Python 3.12
- **فرانت‌اند**: Bootstrap، jQuery
- **پردازش تصویر**: Pillow
- **ترجمه**: django-modeltranslation
- **تقویم**: django-jalali (پشتیبانی تقویم جلالی)
- **درخت دسته‌بندی**: django-mptt
- **رابط مدیریت**: Django Admin با پشتیبانی فونت فارسی

### نصب

#### پیش‌نیازها
- Python 3.12 یا بالاتر
- محیط مجازی (توصیه می‌شود)
- Git

#### دستورالعمل نصب

1. کلون کردن مخزن:
```bash
git clone <repository-url>
cd ArakisSayra
```

2. ایجاد و فعال‌سازی محیط مجازی:
```bash
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
```

3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

4. نصب gettext برای ترجمه‌ها:
```bash
# Ubuntu/Debian
sudo apt-get install gettext

# CentOS/RHEL
sudo yum install gettext
```

5. اجرای مایگریشن‌ها:
```bash
python manage.py migrate
```

6. کامپایل ترجمه‌ها:
```bash
python manage.py compilemessages
```

7. جمع‌آوری فایل‌های استاتیک:
```bash
python manage.py collectstatic
```

8. ایجاد کاربر مدیر:
```bash
python manage.py createsuperuser
```

9. اجرای سرور توسعه:
```bash
python manage.py runserver
```

سایت در آدرس `http://127.0.0.1:8000/` در دسترس خواهد بود

### ساختار پروژه

```
ArakisSayra/
├── ArakisSayra/          # تنظیمات اصلی پروژه
├── blog/                 # اپلیکیشن وبلاگ و اخبار
├── core/                 # عملکرد اصلی و اطلاعات سایت
│   ├── image_optimizer.py
│   ├── management/commands/
│   └── templates/
├── products/             # اپلیکیشن کاتالوگ محصولات
├── contex_processors/    # پردازنده‌های زمینه سفارشی
├── static/               # فایل‌های استاتیک (CSS، JS، تصاویر)
├── media/                # فایل‌های آپلود شده کاربر
├── locale/               # فایل‌های ترجمه
├── docs/                 # مستندات
│   ├── DEPLOYMENT_GUIDE.md
│   ├── IMAGE_OPTIMIZATION_GUIDE.md
│   └── TRANSLATION_GUIDE.md
└── requirements.txt
```

### پیکربندی

#### پیکربندی پایگاه داده

**توسعه (SQLite):**
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

**تولید (MySQL):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'نام_پایگاه_داده',
        'USER': 'کاربر_پایگاه_داده',
        'PASSWORD': 'رمز_عبور',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### پیکربندی فایل‌های استاتیک

**توسعه:**
```python
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

**تولید:**
`STATIC_ROOT` و `MEDIA_ROOT` را به مسیرهای سرور خود به‌روزرسانی کنید.

### دستورات مدیریتی

#### تولید داده‌های نمونه
```bash
python manage.py create_sample_data
```

#### تولید نقشه سایت
```bash
python manage.py generate_sitemap
```

#### به‌روزرسانی ترجمه‌ها
```bash
./update_translations.sh
```

### پنل مدیریت

به پنل مدیریت در آدرس `/admin/` با اعتبارنامه‌های کاربر مدیر دسترسی پیدا کنید.

**ویژگی‌ها:**
- پشتیبانی فونت فارسی
- یکپارچه‌سازی تقویم جلالی
- آپلود تصویر با بهینه‌سازی خودکار
- مدیریت دسته‌بندی با نمای درختی MPTT
- صندوق ورودی پیام برای ارسال‌های فرم تماس

### مستندات

مستندات تفصیلی در پوشه `docs/` موجود است:

- **راهنمای استقرار**: دستورالعمل‌های گام به گام برای استقرار در محیط تولید
- **راهنمای بهینه‌سازی تصویر**: اطلاعات درباره بهینه‌سازی خودکار تصویر
- **راهنمای ترجمه**: نحوه مدیریت و کامپایل ترجمه‌ها

### اندپوینت‌ها

این پروژه به طور پیش‌فرض API REST ندارد، اما تمام محتوا از طریق viewهای Django قابل دسترسی است.

### مشارکت

1. مخزن را فورک کنید
2. یک شاخه ویژگی ایجاد کنید
3. تغییرات خود را کامیت کنید
4. به شاخه پوش کنید
5. یک Pull Request ایجاد کنید

### مجوز

این پروژه تحت مجوز Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) منتشر شده است.

شما آزاد هستید که:
- اشتراک‌گذاری: کپی و توزیع مجدد محتوا در هر رسانه یا قالبی
- تطبیق: ترکیب، تغییر و ساخت بر پایه این محتوا

تحت شرایط زیر:
- انتساب: باید اعتبار مناسب ارائه دهید، لینک مجوز را قرار دهید و نشان دهید که آیا تغییراتی ایجاد شده است
- غیرتجاری: نمی‌توانید از این محتوا برای اهداف تجاری استفاده کنید

برای جزئیات بیشتر، فایل LICENSE را مشاهده کنید یا به آدرس زیر مراجعه کنید: https://creativecommons.org/licenses/by-nc/4.0/deed.fa

### پشتیبانی

برای مشکلات و سوالات، لطفاً با تیم توسعه تماس بگیرید.

---

**Version**: 1.0.0  
**Last Updated**: October 2025  
**Django Version**: 5.2  
**Python Version**: 3.12

