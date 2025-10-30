#!/bin/bash

# اسکریپت Deploy برای Production
# این فایل را روی سرور اجرا کنید

echo "🚀 شروع Deploy..."

# 1. Pull کردن آخرین تغییرات
echo "📥 دریافت تغییرات از Git..."
git pull origin master

# 2. فعال‌سازی Virtual Environment
echo "🐍 فعال‌سازی Virtual Environment..."
source venv/bin/activate

# 3. نصب/بروزرسانی Requirements
echo "📦 بروزرسانی Package ها..."
pip install -r requirements.txt --quiet

# 4. اجرای Migrations
echo "💾 اجرای Migrations..."
python manage.py migrate --noinput

# 5. Collect Static Files
echo "📁 جمع‌آوری فایل‌های Static..."
python manage.py collectstatic --noinput --clear

# 6. Compile Message Files (برای ترجمه)
echo "🌐 کامپایل فایل‌های ترجمه..."
python manage.py compilemessages

# 7. Clear Cache (اگر از cache استفاده می‌کنید)
# python manage.py clear_cache

echo "✅ Deploy با موفقیت انجام شد!"
echo ""
echo "⚠️  حالا باید سرور را Restart کنید:"
echo "   sudo systemctl restart gunicorn"
echo "   sudo systemctl reload nginx"
echo ""
echo "🎉 تمام!"

