# 🚀 راهنمای Deploy تغییرات به Production

## ❓ چرا تغییرات در Production نمایش داده نمی‌شود؟

تغییراتی که انجام دادیم شامل:
- ✅ تغییر template ها (HTML/CSS inline)
- ✅ تغییر فایل‌های CSS (`skin-corporate-5.css`)
- ✅ تغییر فایل‌های Python (views, urls)

---

## 📋 مراحل Deploy به Production:

### مرحله 1️⃣: Push کردن تغییرات (در Local)

```bash
# بررسی فایل‌های تغییر یافته
git status

# اضافه کردن تمام تغییرات
git add .

# Commit کردن
git commit -m "بهبود UI صفحه جزئیات محصول و تغییر فونت به وزیر"

# Push به سرور
git push origin master
```

---

### مرحله 2️⃣: دریافت تغییرات در Production

**SSH به سرور Production:**
```bash
ssh username@arakissayra.ir
```

**رفتن به دایرکتوری پروژه:**
```bash
cd /home/arakissa/public_html/
# یا هر مسیری که پروژه شماست
```

**Pull کردن تغییرات:**
```bash
git pull origin master
```

---

### مرحله 3️⃣: Collect Static Files

اگر فایل CSS یا JavaScript تغییر کرده:

```bash
source venv/bin/activate
python manage.py collectstatic --noinput --clear
```

**⚠️ نکته مهم:** چون فایل `skin-corporate-5.css` تغییر کرده، این مرحله **حتماً** باید اجرا شود!

---

### مرحله 4️⃣: Restart کردن سرور (خیلی مهم! ⚠️)

**اگر از Gunicorn استفاده می‌کنید:**
```bash
sudo systemctl restart gunicorn
# یا
sudo supervisorctl restart your-app-name
```

**اگر از Apache استفاده می‌کنید:**
```bash
sudo systemctl restart apache2
# یا
sudo service apache2 restart
```

**اگر از Nginx + uWSGI استفاده می‌کنید:**
```bash
sudo systemctl restart uwsgi
sudo systemctl reload nginx
```

---

### مرحله 5️⃣: پاک کردن Cache مرورگر

در مرورگر:
- **Chrome/Firefox:** `Ctrl + Shift + R` یا `Ctrl + F5`
- **Mac:** `Cmd + Shift + R`

---

## 🎯 اسکریپت خودکار Deploy

یک اسکریپت آماده ساختم که همه مراحل رو خودکار انجام می‌ده:

```bash
# در سرور Production اجرا کنید:
./deploy_production.sh
```

بعد فقط باید سرور رو Restart کنید:
```bash
sudo systemctl restart gunicorn
sudo systemctl reload nginx
```

---

## 🔧 رفع مشکلات رایج:

### مشکل 1: تغییرات CSS نمایش داده نمی‌شود
**علت:** Static files جمع‌آوری نشده  
**راه‌حل:**
```bash
python manage.py collectstatic --noinput --clear
```

### مشکل 2: تغییرات Template نمایش داده نمی‌شود
**علت:** سرور restart نشده  
**راه‌حل:**
```bash
sudo systemctl restart gunicorn
```

### مشکل 3: تصاویر نمایش داده نمی‌شود
**علت:** MEDIA_URL در production درست تنظیم نشده  
**راه‌حل:** در `urls.py` این خط رو اضافه کردیم:
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### مشکل 4: هنوز تغییرات نیست!
**راه‌حل:** Hard Refresh در مرورگر
```
Ctrl + Shift + Delete → Clear Cache
```

---

## ✅ چک‌لیست نهایی:

- [ ] Git pull در سرور
- [ ] collectstatic اجرا شده
- [ ] سرور Restart شده
- [ ] Cache مرورگر پاک شده
- [ ] Nginx/Apache reload شده

---

## 📞 در صورت مشکل:

1. لاگ‌های سرور را بررسی کنید:
```bash
# Gunicorn logs
sudo journalctl -u gunicorn -f

# Nginx logs
sudo tail -f /var/log/nginx/error.log

# Apache logs
sudo tail -f /var/log/apache2/error.log
```

2. مطمئن شوید DEBUG=False در production است
3. مطمئن شوید STATIC_ROOT و MEDIA_ROOT درست تنظیم شده

---

## 🎊 نتیجه:

بعد از انجام این مراحل، تغییرات شما باید در Production نمایش داده شود!

