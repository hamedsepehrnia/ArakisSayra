<div align="center">

# Arakis Sayra

**A Modern Bilingual E-commerce Platform Built with Django**

[![Persian](https://img.shields.io/badge/lang-persian-blue?style=for-the-badge)](#فارسی)
[![English](https://img.shields.io/badge/lang-English-green?style=for-the-badge)](#english)

---

### ☕ Support This Project | حمایت از این پروژه

<div align="center">

#### حمایت با پول ایرانی | Support with Iranian Rial
  
<a href="https://www.coffeebede.com/hamesep">
  <img src="https://coffeebede.ir/DashboardTemplateV2/app-assets/images/banner/default-yellow.svg" alt="Buy Me A Coffee" height="60">
</a>

#### حمایت با ارزهای دیجیتال | Crypto Donations

<a href="https://nowpayments.io/donation?api_key=19623fa3-605a-436a-97cd-b5859356b41d" target="_blank">
  <img src="https://img.shields.io/badge/Donate-Crypto-blue?style=for-the-badge&logo=bitcoin&logoColor=white" alt="Donate with Crypto" height="50">
</a>

**Supported:** Bitcoin, Ethereum, USDT, BNB, and 100+ cryptocurrencies

</div>

---

</div>

## English

### Overview

A bilingual (Persian/English) e-commerce platform built with Django 5.2. Includes product catalog, blog, and content management features with support for Persian language and Jalali calendar.

### Features

#### Multilingual Support
- Persian and English language support
- Content translation using django-modeltranslation
- Language-based URL routing
- RTL/LTR layout support

#### Product Management
- Hierarchical category system (django-mptt)
- Product catalog with specifications
- SEO-friendly URLs
- Category-based filtering

#### Content Management
- Blog and news sections
- Category organization
- Jalali calendar integration
- Multiple authors support

#### Image Optimization
- Automatic image resizing and compression
- Progressive JPEG encoding
- Configurable quality (85-88%)
- Standard dimensions for different content types

#### Security & Configuration
- Environment variables for sensitive data (python-decouple)
- Secure credential management
- Separate development and production configs
- Dynamic site information management
- Contact form with validation
- Banner management
- Social media links

### Technology Stack

| Component | Technology |
|-----------|-----------|
| Framework | Django 5.2 |
| Language | Python 3.12 |
| Database | SQLite / MySQL |
| Frontend | Bootstrap, jQuery |
| Image Processing | Pillow |
| Translation | django-modeltranslation |
| Calendar | django-jalali |
| Category Trees | django-mptt |
| Configuration | python-decouple |
| Admin Interface | Django Admin |

### Installation

#### Prerequisites
- Python 3.12 or higher
- Git
- gettext (for translations)

#### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ArakisSayra.git
cd ArakisSayra
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup environment variables:
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your actual credentials
nano .env  # or use your preferred editor
```

**Important:** Configure these variables in `.env`:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (False for production)
- `ALLOWED_HOSTS` - Your domain names
- `DB_NAME`, `DB_USER`, `DB_PASSWORD` - Database credentials
- `STATIC_ROOT`, `MEDIA_ROOT` - File storage paths

See [ENV_SETUP.md](ENV_SETUP.md) for detailed instructions.

5. Install gettext:
```bash
# Ubuntu/Debian
sudo apt-get install gettext

# macOS
brew install gettext

# CentOS/RHEL
sudo yum install gettext
```

6. Setup database and static files:
```bash
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
```

7. Create admin user:
```bash
python manage.py createsuperuser
```

8. (Optional) Load sample data:
```bash
python manage.py create_sample_data
```

9. Run development server:
```bash
python manage.py runserver
```

Access the site at `http://127.0.0.1:8000/`  
Admin panel at `http://127.0.0.1:8000/admin/`

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
├── .env                  # Environment variables (not in git)
├── .env.example          # Environment variables template
├── ENV_SETUP.md          # Environment setup guide
└── requirements.txt
```

### Configuration

#### Environment Variables

This project uses **python-decouple** for secure configuration management. All sensitive data is stored in environment variables.

**Setup `.env` file:**
```bash
cp .env.example .env
# Edit .env with your actual values
```

**Required variables:**
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306

# Static and Media Files
STATIC_ROOT=/path/to/static
MEDIA_ROOT=/path/to/media
```

**Security Notes:**
- ⚠️ Never commit `.env` file to version control
- Generate a strong `SECRET_KEY` for production
- Keep `DEBUG=False` in production
- Use strong database passwords

For detailed setup instructions, see [ENV_SETUP.md](ENV_SETUP.md)

#### Database Configuration

The database is configured via environment variables in `.env`:

**Development (SQLite):**
```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

**Production (MySQL):**
```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=3306
```

#### Static Files Configuration

Configure via environment variables:

**Development:**
```env
STATIC_ROOT=./staticfiles
MEDIA_ROOT=./media
```

**Production:**
```env
STATIC_ROOT=/home/user/public_html/static
MEDIA_ROOT=/home/user/public_html/media
```

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

Detailed documentation is available in the project:

- **[ENV_SETUP.md](ENV_SETUP.md)**: Complete guide for environment variables setup
- **[DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md)**: Step-by-step deployment instructions
- **[IMAGE_OPTIMIZATION_GUIDE.md](docs/IMAGE_OPTIMIZATION_GUIDE.md)**: Automatic image optimization details
- **[TRANSLATION_GUIDE.md](docs/TRANSLATION_GUIDE.md)**: Translation management guide

### Endpoints

The project doesn't have a REST API by default, but all content is accessible through Django views.

### Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature/feature-name`
5. Open a Pull Request

### License

This project is licensed under CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0).

- You may share and adapt the material
- You must give appropriate credit
- Non-commercial use only

Full license: [LICENSE](LICENSE) | https://creativecommons.org/licenses/by-nc/4.0/

### Support

- Issues: [GitHub Issues](https://github.com/yourusername/ArakisSayra/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/ArakisSayra/discussions)
- Donations: [CoffeeBede](https://www.coffeebede.com/hamesep) | [Crypto](https://nowpayments.io/donation?api_key=19623fa3-605a-436a-97cd-b5859356b41d)

---

## فارسی

### معرفی

پلتفرم فروشگاهی دوزبانه (فارسی/انگلیسی) ساخته شده با Django 5.2. شامل مدیریت کاتالوگ محصولات، وبلاگ و سیستم مدیریت محتوا با پشتیبانی از زبان فارسی و تقویم جلالی.

### ویژگی‌ها

#### پشتیبانی چندزبانه
- پشتیبانی از زبان‌های فارسی و انگلیسی
- ترجمه محتوا با استفاده از django-modeltranslation
- مسیریابی URL بر اساس زبان
- پشتیبانی از چیدمان راست‌به‌چپ و چپ‌به‌راست

#### مدیریت محصولات
- سیستم دسته‌بندی سلسله‌مراتبی (django-mptt)
- کاتالوگ محصولات با مشخصات
- URLهای سئو شده
- فیلترینگ بر اساس دسته‌بندی

#### مدیریت محتوا
- بخش‌های وبلاگ و اخبار
- سازماندهی بر اساس دسته‌بندی
- یکپارچه‌سازی تقویم جلالی
- پشتیبانی از چند نویسنده

#### بهینه‌سازی تصاویر
- تغییر اندازه و فشرده‌سازی خودکار تصاویر
- کدگذاری Progressive JPEG
- کیفیت قابل تنظیم (85-88%)
- ابعاد استاندارد برای انواع محتوا

#### امنیت و پیکربندی
- متغیرهای محیطی برای داده‌های حساس (python-decouple)
- مدیریت امن اعتبارنامه‌ها
- پیکربندی جداگانه برای توسعه و تولید
- مدیریت پویای اطلاعات سایت
- فرم تماس با اعتبارسنجی
- مدیریت بنر
- لینک‌های شبکه‌های اجتماعی

### پشته فناوری

| بخش | تکنولوژی |
|-----|-----------|
| فریمورک | Django 5.2 |
| زبان برنامه‌نویسی | Python 3.12 |
| پایگاه داده | SQLite / MySQL |
| فرانت‌اند | Bootstrap، jQuery |
| پردازش تصویر | Pillow |
| ترجمه | django-modeltranslation |
| تقویم | django-jalali |
| درخت دسته‌بندی | django-mptt |
| پیکربندی | python-decouple |
| رابط مدیریت | Django Admin |

### نصب و راه‌اندازی

#### پیش‌نیازها
- Python 3.12 یا بالاتر
- Git
- gettext (برای ترجمه‌ها)

#### مراحل نصب

1. کلون کردن ریپازیتوری:
```bash
git clone https://github.com/yourusername/ArakisSayra.git
cd ArakisSayra
```

2. ایجاد و فعال‌سازی محیط مجازی:
```bash
python -m venv venv
source venv/bin/activate  # ویندوز: venv\Scripts\activate
```

3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

4. تنظیم متغیرهای محیطی:
```bash
# کپی کردن فایل نمونه
cp .env.example .env

# ویرایش .env با اطلاعات واقعی
nano .env  # یا از ویرایشگر دلخواه خود استفاده کنید
```

**مهم:** این متغیرها را در `.env` پیکربندی کنید:
- `SECRET_KEY` - کلید مخفی Django
- `DEBUG` - حالت دیباگ (False برای تولید)
- `ALLOWED_HOSTS` - نام دامنه‌های شما
- `DB_NAME`, `DB_USER`, `DB_PASSWORD` - اعتبارنامه‌های دیتابیس
- `STATIC_ROOT`, `MEDIA_ROOT` - مسیرهای ذخیره‌سازی فایل

برای دستورالعمل کامل [ENV_SETUP.md](ENV_SETUP.md) را ببینید.

5. نصب gettext:
```bash
# Ubuntu/Debian
sudo apt-get install gettext

# macOS
brew install gettext

# CentOS/RHEL
sudo yum install gettext
```

6. راه‌اندازی پایگاه داده و فایل‌های استاتیک:
```bash
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
```

7. ایجاد کاربر مدیر:
```bash
python manage.py createsuperuser
```

8. (اختیاری) بارگذاری داده‌های نمونه:
```bash
python manage.py create_sample_data
```

9. اجرای سرور توسعه:
```bash
python manage.py runserver
```

دسترسی به سایت در `http://127.0.0.1:8000/`  
پنل مدیریت در `http://127.0.0.1:8000/admin/`

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
├── .env                  # متغیرهای محیطی (در گیت نیست)
├── .env.example          # الگوی متغیرهای محیطی
├── ENV_SETUP.md          # راهنمای تنظیم متغیرهای محیطی
└── requirements.txt
```

### پیکربندی

#### متغیرهای محیطی

این پروژه از **python-decouple** برای مدیریت امن پیکربندی استفاده می‌کند. تمام داده‌های حساس در متغیرهای محیطی ذخیره می‌شوند.

**راه‌اندازی فایل `.env`:**
```bash
cp .env.example .env
# ویرایش .env با مقادیر واقعی شما
```

**متغیرهای مورد نیاز:**
```env
# تنظیمات Django
SECRET_KEY=کلید-مخفی-شما
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# پیکربندی پایگاه داده
DB_ENGINE=django.db.backends.mysql
DB_NAME=نام_پایگاه_داده
DB_USER=کاربر_پایگاه_داده
DB_PASSWORD=رمز_عبور_پایگاه_داده
DB_HOST=localhost
DB_PORT=3306

# فایل‌های استاتیک و مدیا
STATIC_ROOT=/path/to/static
MEDIA_ROOT=/path/to/media
```

**نکات امنیتی:**
- ⚠️ هرگز فایل `.env` را به کنترل نسخه commit نکنید
- یک `SECRET_KEY` قوی برای محیط تولید تولید کنید
- `DEBUG=False` را در محیط تولید نگه دارید
- از رمزهای عبور قوی برای دیتابیس استفاده کنید

برای دستورالعمل کامل راه‌اندازی، [ENV_SETUP.md](ENV_SETUP.md) را ببینید

#### پیکربندی پایگاه داده

پایگاه داده از طریق متغیرهای محیطی در `.env` پیکربندی می‌شود:

**توسعه (SQLite):**
```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

**تولید (MySQL):**
```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=نام_پایگاه_داده
DB_USER=کاربر_پایگاه_داده
DB_PASSWORD=رمز_عبور_امن
DB_HOST=localhost
DB_PORT=3306
```

#### پیکربندی فایل‌های استاتیک

پیکربندی از طریق متغیرهای محیطی:

**توسعه:**
```env
STATIC_ROOT=./staticfiles
MEDIA_ROOT=./media
```

**تولید:**
```env
STATIC_ROOT=/home/user/public_html/static
MEDIA_ROOT=/home/user/public_html/media
```

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

مستندات تفصیلی در پروژه موجود است:

- **[ENV_SETUP.md](ENV_SETUP.md)**: راهنمای کامل راه‌اندازی متغیرهای محیطی
- **[DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md)**: دستورالعمل‌های گام به گام استقرار
- **[IMAGE_OPTIMIZATION_GUIDE.md](docs/IMAGE_OPTIMIZATION_GUIDE.md)**: جزئیات بهینه‌سازی خودکار تصویر
- **[TRANSLATION_GUIDE.md](docs/TRANSLATION_GUIDE.md)**: راهنمای مدیریت ترجمه

### اندپوینت‌ها

این پروژه به طور پیش‌فرض API REST ندارد، اما تمام محتوا از طریق viewهای Django قابل دسترسی است.

### مشارکت

مشارکت‌ها خوشایند است. لطفاً این مراحل را دنبال کنید:

1. ریپازیتوری را فورک کنید
2. یک شاخه ویژگی ایجاد کنید: `git checkout -b feature/feature-name`
3. تغییرات را کامیت کنید: `git commit -m 'Add feature'`
4. به شاخه پوش کنید: `git push origin feature/feature-name`
5. یک Pull Request باز کنید

### مجوز

این پروژه تحت مجوز CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0) منتشر شده است.

- می‌توانید مطالب را به اشتراک بگذارید و تغییر دهید
- باید اعتبار مناسب ارائه دهید
- فقط برای استفاده غیرتجاری

مجوز کامل: [LICENSE](LICENSE) | https://creativecommons.org/licenses/by-nc/4.0/deed.fa

### پشتیبانی

- گزارش مشکلات: [GitHub Issues](https://github.com/yourusername/ArakisSayra/issues)
- بحث و گفتگو: [GitHub Discussions](https://github.com/yourusername/ArakisSayra/discussions)
- حمایت مالی: [کافی بده](https://www.coffeebede.com/hamesep) | [کریپتو](https://nowpayments.io/donation?api_key=19623fa3-605a-436a-97cd-b5859356b41d)

---

<div align="center">

**Version** 1.0.0 | **Django** 5.2 | **Python** 3.12

<img src="https://img.shields.io/badge/Django-5.2-green?style=flat-square&logo=django" alt="Django">
<img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python" alt="Python">
<img src="https://img.shields.io/badge/Bootstrap-5-purple?style=flat-square&logo=bootstrap" alt="Bootstrap">
<img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-orange?style=flat-square" alt="License">

---

© 2025 Arakis Sayra

</div>

