# 🌍 راهنمای کامپایل ترجمه‌ها

## 📋 ترجمه‌های اضافه شده:

تمام متن‌های صفحات زیر به فایل `locale/en/LC_MESSAGES/django.po` اضافه شدند:

### صفحه درباره ما:
- ✅ معرفی شرکت
- ✅ چرا آراکیس سایرا؟
- ✅ کیفیت تضمین شده
- ✅ سازگار با محیط زیست
- ✅ نوآوری مستمر
- ✅ تیم متخصص
- ✅ سال تجربه
- ✅ محصول متنوع
- ✅ مشتری راضی
- ✅ گواهینامه‌های معتبر
- ✅ ارزش‌های ما
- ✅ کیفیت، اعتماد، پایداری
- ✅ CTA متن‌ها

### صفحه تماس با ما:
- ✅ ارسال پیام
- ✅ اطلاعات تماس
- ✅ تلفن‌های تماس
- ✅ اینستاگرام
- ✅ ساعات کاری
- ✅ پیام‌های موفقیت و خطا

### عمومی:
- ✅ مشاهده جزئیات
- ✅ ادامه مطلب
- ✅ نتایج جستجو
- ✅ منو
- ✅ و بیشتر...

---

## 🚀 نحوه اعمال ترجمه‌ها:

### روش 1: استفاده از اسکریپت آماده (ساده‌ترین)

```bash
# اجرای اسکریپت
./update_translations.sh
```

این اسکریپت به صورت خودکار:
1. gettext را نصب می‌کند (اگر نصب نباشد)
2. Virtual environment را فعال می‌کند
3. ترجمه‌ها را کامپایل می‌کند

---

### روش 2: دستی (گام به گام)

#### مرحله 1: نصب gettext

```bash
sudo apt-get update
sudo apt-get install -y gettext
```

#### مرحله 2: کامپایل ترجمه‌ها

```bash
cd /home/hamed/Desktop/ArakisSayra
source venv/bin/activate
python manage.py compilemessages
```

#### مرحله 3: Restart سرور

```bash
# اگر در development
# فقط سرور را متوقف کنید (Ctrl+C) و دوباره اجرا کنید:
python manage.py runserver

# اگر در production
sudo systemctl restart gunicorn
sudo systemctl reload nginx
```

---

## 📝 خروجی موفق:

بعد از اجرای `compilemessages` باید چیزی شبیه این ببینید:

```
processing file django.po in /path/to/locale/en/LC_MESSAGES
compiling message catalog django.mo
```

---

## ✅ بررسی نتیجه:

1. مرورگر را باز کنید
2. به نسخه انگلیسی سایت بروید (کلیک روی English)
3. صفحات زیر را بررسی کنید:
   - درباره ما
   - تماس با ما
   - محصولات
   - بلاگ
   - اخبار

---

## 🔧 رفع مشکل:

### مشکل 1: gettext نصب نمی‌شود
```bash
# در Ubuntu/Debian:
sudo apt-get install gettext

# در CentOS/RHEL:
sudo yum install gettext
```

### مشکل 2: ترجمه‌ها نمایش داده نمی‌شوند
```bash
# مطمئن شوید که:
1. فایل django.mo ساخته شده است
2. سرور restart شده است
3. Cache مرورگر پاک شده است (Ctrl+F5)
```

### مشکل 3: بعضی متن‌ها ترجمه نشده‌اند
```bash
# دوباره ترجمه‌ها را کامپایل کنید:
python manage.py compilemessages --ignore=venv

# و سرور را restart کنید
```

---

## 📦 فایل‌های مهم:

- `locale/en/LC_MESSAGES/django.po` - فایل ترجمه (قابل ویرایش)
- `locale/en/LC_MESSAGES/django.mo` - فایل کامپایل شده (خودکار ساخته می‌شود)

---

## 💡 نکته مهم:

**همیشه بعد از تغییر فایل `.po` باید:**
1. ✅ `compilemessages` اجرا شود
2. ✅ سرور restart شود
3. ✅ مرورگر Hard Refresh شود

---

## 🎯 نتیجه:

بعد از اعمال این تغییرات، **تمام صفحات سایت در نسخه انگلیسی** به درستی ترجمه می‌شوند! 🌐

