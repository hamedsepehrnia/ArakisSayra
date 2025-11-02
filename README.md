<div align="center">

# 🌟 Arakis Sayra

**A Modern Bilingual E-commerce Platform Built with Django**

[![Persian](https://img.shields.io/badge/lang-فارسی-blue?style=for-the-badge)](#-persian)
[![English](https://img.shields.io/badge/lang-English-green?style=for-the-badge)](#-english)

---

### ☕ Support This Project | حمایت از این پروژه

<div align="center">

#### 💳 حمایت با پول ایرانی | Support with Iranian Rial
  
<a href="https://www.coffeebede.com/hamesep">
  <img src="https://coffeebede.ir/DashboardTemplateV2/app-assets/images/banner/default-yellow.svg" alt="Buy Me A Coffee" height="60">
</a>

#### 🪙 حمایت با ارزهای دیجیتال | Crypto Donations

<a href="https://nowpayments.io/donation?api_key=19623fa3-605a-436a-97cd-b5859356b41d" target="_blank">
  <img src="https://img.shields.io/badge/Donate-Crypto-blue?style=for-the-badge&logo=bitcoin&logoColor=white" alt="Donate with Crypto" height="50">
</a>

**Supported:** Bitcoin, Ethereum, USDT, BNB, and 100+ cryptocurrencies

</div>

---

</div>

## 🇬🇧 English

### 📖 Overview

Arakis Sayra is a **powerful, production-ready** bilingual (Persian/English) e-commerce platform built with **Django 5.2**. 

This isn't just another Django project - it's a complete business solution that combines:
- 🛍️ A sophisticated product catalog system
- 📝 Built-in blogging and news management
- 🌐 True bilingual support (not just UI translation)
- 📱 Beautiful, responsive design
- 🚀 Production-ready features out of the box

Perfect for businesses looking to reach both Persian and English-speaking markets!

### ✨ Key Features

#### 🌐 Multilingual Support
What makes this special? It's not just translated UI elements - **every piece of content** can be managed in both languages:
- Full Persian (Farsi) and English language support
- Django modeltranslation for seamless content translation
- Smart URL routing based on language selection
- RTL/LTR layout switching

#### 🛍️ Product Management
Built for real businesses with complex catalogs:
- **Hierarchical category system** using Django MPTT (unlimited nesting!)
- Rich product specifications and details
- SEO-friendly automatic slug generation
- Smart image optimization (your images load fast!)
- Advanced category-based filtering

#### 📝 Content Management
More than just an e-commerce site:
- Full-featured blog with rich text editor
- News section for company announcements
- Category-based organization
- **Jalali calendar** support for Persian dates
- Multi-author system

#### 🖼️ Intelligent Image Optimization
Your images will look great **and** load fast:
- Automatic resizing and compression on upload
- Progressive JPEG encoding
- Smart quality settings (85-88%)
- Pre-configured dimensions:
  - Banners: 1920×960 pixels
  - Products: 1000×1000 pixels
  - Blog/News: 900×585 pixels
  - About section: 800×600 pixels

#### ⚙️ Site Management
Everything you need to run a professional website:
- Dynamic site information (no code changes needed!)
- Contact form with admin inbox
- Banner management system
- Customizable working hours and contact details
- Social media integration (Instagram, and more)

### 🛠️ Technology Stack

Built with modern, battle-tested technologies:

| Category | Technology | Why? |
|----------|-----------|------|
| **Framework** | Django 5.2 | Latest stable version, secure & scalable |
| **Language** | Python 3.12 | Modern Python with latest features |
| **Database** | SQLite / MySQL | Flexible: easy development, powerful production |
| **Frontend** | Bootstrap + jQuery | Responsive, mobile-first design |
| **Image Processing** | Pillow | Automatic optimization on upload |
| **Translation** | django-modeltranslation | True bilingual content management |
| **Calendar** | django-jalali | Native Jalali (Persian) calendar support |
| **Category Trees** | django-mptt | Efficient hierarchical data |
| **Admin** | Django Admin | Customized with Persian font support |

### 🚀 Quick Start

#### Prerequisites
Make sure you have these installed:
- ✅ Python 3.12 or higher
- ✅ Git
- ✅ gettext (for translations)

#### Installation (5 Minutes Setup!)

**1️⃣ Clone and enter the project:**
```bash
git clone https://github.com/yourusername/ArakisSayra.git
cd ArakisSayra
```

**2️⃣ Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3️⃣ Install dependencies:**
```bash
pip install -r requirements.txt
```

**4️⃣ Install gettext (for translations):**
```bash
# Ubuntu/Debian
sudo apt-get install gettext

# macOS
brew install gettext

# CentOS/RHEL
sudo yum install gettext
```

**5️⃣ Setup database:**
```bash
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
```

**6️⃣ Create admin user:**
```bash
python manage.py createsuperuser
```

**7️⃣ (Optional) Load sample data:**
```bash
python manage.py create_sample_data
```

**8️⃣ Run the server:**
```bash
python manage.py runserver
```

**🎉 Done!** Visit `http://127.0.0.1:8000/` to see your site!  
Admin panel: `http://127.0.0.1:8000/admin/`

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

### 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

Please make sure your code follows the existing style and includes tests where appropriate.

### 📄 License

This project is licensed under **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0).

**You can:**
- ✅ Share and redistribute
- ✅ Adapt and build upon it
- ✅ Use for personal projects

**You must:**
- 📝 Give appropriate credit
- 🔗 Link to the license
- ⚠️ Indicate changes made

**You cannot:**
- ❌ Use for commercial purposes without permission

📚 Full license: [LICENSE](LICENSE) | https://creativecommons.org/licenses/by-nc/4.0/

### 💬 Support & Questions

- 🐛 **Found a bug?** [Open an issue](https://github.com/yourusername/ArakisSayra/issues)
- 💡 **Have a feature request?** [Start a discussion](https://github.com/yourusername/ArakisSayra/discussions)
- 📧 **Need help?** Contact the development team

---

### ⭐ If You Like This Project

Please consider:
- ⭐ **Starring** this repository
- ☕ **Supporting** via [CoffeeBede](https://www.coffeebede.com/hamesep)
- 🔄 **Sharing** with others who might benefit

---

## 🇮🇷 فارسی

### 📖 معرفی

آراکیس سایرا یک پلتفرم **قدرتمند و آماده تولید** برای تجارت الکترونیک دوزبانه (فارسی/انگلیسی) است که با **Django 5.2** ساخته شده.

این فقط یک پروژه Django معمولی نیست - این یک راه‌حل کامل کسب‌وکار است که ترکیبی از این موارد را ارائه می‌دهد:
- 🛍️ سیستم پیشرفته کاتالوگ محصولات
- 📝 مدیریت وبلاگ و اخبار داخلی
- 🌐 پشتیبانی واقعی دوزبانه (نه فقط ترجمه رابط کاربری!)
- 📱 طراحی زیبا و ریسپانسیو
- 🚀 قابلیت‌های آماده برای محیط تولید

انتخاب ایده‌آل برای کسب‌وکارهایی که می‌خواهند به بازارهای فارسی‌زبان و انگلیسی‌زبان دسترسی داشته باشند!

### ✨ ویژگی‌های کلیدی

#### 🌐 پشتیبانی چندزبانه
چه چیزی این پروژه را متمایز می‌کند؟ این فقط ترجمه المان‌های رابط کاربری نیست - **تمام محتوا** در هر دو زبان قابل مدیریت است:
- پشتیبانی کامل از زبان‌های فارسی و انگلیسی
- django-modeltranslation برای ترجمه یکپارچه محتوا
- مسیریابی هوشمند URL بر اساس انتخاب زبان
- تغییر خودکار بین چیدمان راست‌به‌چپ و چپ‌به‌راست

#### 🛍️ مدیریت محصولات
ساخته شده برای کسب‌وکارهای واقعی با کاتالوگ‌های پیچیده:
- **سیستم دسته‌بندی سلسله‌مراتبی** با استفاده از Django MPTT (تو در تو نامحدود!)
- مشخصات و جزئیات غنی محصولات
- تولید خودکار اسلاگ سئو شده
- بهینه‌سازی هوشمند تصاویر (تصاویر شما سریع لود می‌شوند!)
- فیلترینگ پیشرفته بر اساس دسته‌بندی

#### 📝 مدیریت محتوا
بیشتر از یک سایت فروشگاهی ساده:
- وبلاگ کامل با ویرایشگر متن غنی
- بخش اخبار برای اطلاعیه‌های شرکت
- سازماندهی بر اساس دسته‌بندی
- پشتیبانی از **تقویم جلالی** برای تاریخ‌های شمسی
- سیستم چند نویسنده

#### 🖼️ بهینه‌سازی هوشمند تصاویر
تصاویر شما هم زیبا هستند **و هم** سریع لود می‌شوند:
- تغییر اندازه و فشرده‌سازی خودکار در زمان آپلود
- کدگذاری Progressive JPEG
- تنظیمات هوشمند کیفیت (85-88%)
- ابعاد از پیش تنظیم شده:
  - بنرها: 1920×960 پیکسل
  - محصولات: 1000×1000 پیکسل
  - بلاگ/اخبار: 900×585 پیکسل
  - بخش درباره ما: 800×600 پیکسل

#### ⚙️ مدیریت سایت
همه چیزی که برای اداره یک وب‌سایت حرفه‌ای نیاز دارید:
- مدیریت پویای اطلاعات سایت (نیازی به تغییر کد نیست!)
- فرم تماس با صندوق ورودی در پنل ادمین
- سیستم مدیریت بنر
- ساعات کاری و اطلاعات تماس قابل تنظیم
- یکپارچه‌سازی شبکه‌های اجتماعی (اینستاگرام و بیشتر)

### 🛠️ پشته فناوری

ساخته شده با تکنولوژی‌های مدرن و آزمایش شده:

| دسته‌بندی | تکنولوژی | چرا؟ |
|----------|-----------|------|
| **فریمورک** | Django 5.2 | آخرین نسخه پایدار، امن و مقیاس‌پذیر |
| **زبان** | Python 3.12 | پایتون مدرن با آخرین قابلیت‌ها |
| **پایگاه داده** | SQLite / MySQL | انعطاف‌پذیر: توسعه آسان، تولید قدرتمند |
| **فرانت‌اند** | Bootstrap + jQuery | طراحی ریسپانسیو و موبایل‌محور |
| **پردازش تصویر** | Pillow | بهینه‌سازی خودکار در زمان آپلود |
| **ترجمه** | django-modeltranslation | مدیریت واقعی محتوای دوزبانه |
| **تقویم** | django-jalali | پشتیبانی بومی از تقویم جلالی |
| **درخت دسته‌بندی** | django-mptt | داده‌های سلسله‌مراتبی کارآمد |
| **پنل ادمین** | Django Admin | سفارشی‌سازی شده با پشتیبانی فونت فارسی |

### 🚀 شروع سریع

#### پیش‌نیازها
مطمئن شوید این‌ها نصب شده‌اند:
- ✅ Python 3.12 یا بالاتر
- ✅ Git
- ✅ gettext (برای ترجمه‌ها)

#### نصب (راه‌اندازی در 5 دقیقه!)

**1️⃣ کلون و ورود به پروژه:**
```bash
git clone https://github.com/yourusername/ArakisSayra.git
cd ArakisSayra
```

**2️⃣ ایجاد محیط مجازی:**
```bash
python -m venv venv
source venv/bin/activate  # ویندوز: venv\Scripts\activate
```

**3️⃣ نصب وابستگی‌ها:**
```bash
pip install -r requirements.txt
```

**4️⃣ نصب gettext (برای ترجمه‌ها):**
```bash
# Ubuntu/Debian
sudo apt-get install gettext

# macOS
brew install gettext

# CentOS/RHEL
sudo yum install gettext
```

**5️⃣ راه‌اندازی پایگاه داده:**
```bash
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
```

**6️⃣ ایجاد کاربر مدیر:**
```bash
python manage.py createsuperuser
```

**7️⃣ (اختیاری) بارگذاری داده‌های نمونه:**
```bash
python manage.py create_sample_data
```

**8️⃣ اجرای سرور:**
```bash
python manage.py runserver
```

**🎉 تمام!** برای دیدن سایت به `http://127.0.0.1:8000/` بروید!  
پنل ادمین: `http://127.0.0.1:8000/admin/`

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

### 🤝 مشارکت

ما از مشارکت شما استقبال می‌کنیم! اینطور می‌توانید مشارکت کنید:

1. مخزن را **فورک** کنید
2. یک شاخه ویژگی **ایجاد** کنید: `git checkout -b feature/ویژگی-شگفت‌انگیز`
3. تغییرات را **کامیت** کنید: `git commit -m 'افزودن ویژگی شگفت‌انگیز'`
4. به شاخه **پوش** کنید: `git push origin feature/ویژگی-شگفت‌انگیز`
5. یک Pull Request **باز** کنید

لطفاً مطمئن شوید کدتان از استایل موجود پیروی می‌کند و در صورت نیاز تست‌های لازم را شامل می‌شود.

### 📄 مجوز

این پروژه تحت مجوز **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0) منتشر شده است.

**می‌توانید:**
- ✅ به اشتراک بگذارید و توزیع کنید
- ✅ تغییر دهید و بر اساس آن بسازید
- ✅ برای پروژه‌های شخصی استفاده کنید

**باید:**
- 📝 اعتبار مناسب ارائه دهید
- 🔗 لینک مجوز را قرار دهید
- ⚠️ تغییرات انجام شده را نشان دهید

**نمی‌توانید:**
- ❌ بدون مجوز برای اهداف تجاری استفاده کنید

📚 مجوز کامل: [LICENSE](LICENSE) | https://creativecommons.org/licenses/by-nc/4.0/deed.fa

### 💬 پشتیبانی و سوالات

- 🐛 **باگ پیدا کردید؟** [یک issue باز کنید](https://github.com/yourusername/ArakisSayra/issues)
- 💡 **درخواست ویژگی دارید؟** [بحثی شروع کنید](https://github.com/yourusername/ArakisSayra/discussions)
- 📧 **نیاز به کمک دارید؟** با تیم توسعه تماس بگیرید

---

### ⭐ اگر این پروژه را دوست دارید

لطفاً در نظر بگیرید:
- ⭐ **ستاره دادن** به این ریپازیتوری
- ☕ **حمایت** از طریق [کافی بده](https://www.coffeebede.com/hamesep)
- 🔄 **اشتراک‌گذاری** با دیگرانی که ممکن است استفاده کنند

---

<div align="center">

### 📊 نسخه و اطلاعات | Version Info

| | |
|:---:|:---:|
| **Version** / **نسخه** | 1.0.0 |
| **Last Updated** / **آخرین به‌روزرسانی** | November 2025 |
| **Django Version** / **نسخه جنگو** | 5.2 |
| **Python Version** / **نسخه پایتون** | 3.12 |
| **License** / **مجوز** | CC BY-NC 4.0 |

---

### 💖 ساخته شده با عشق | Made with Love

<p>
  <img src="https://img.shields.io/badge/Django-5.2-green?style=flat-square&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Bootstrap-5-purple?style=flat-square&logo=bootstrap" alt="Bootstrap">
  <img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-orange?style=flat-square" alt="License">
</p>

**اگر این پروژه برایتان مفید بود، یک ⭐ فراموش نشود!**  
**If you found this project helpful, don't forget to ⭐ it!**

---

**© 2025 Arakis Sayra | آراکیس سایرا**

</div>

