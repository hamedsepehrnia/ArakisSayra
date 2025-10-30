#!/bin/bash

# اسکریپت بروزرسانی ترجمه‌ها

echo "🌍 بروزرسانی ترجمه‌های سایت..."

# 1. بررسی وجود gettext
if ! command -v msgfmt &> /dev/null; then
    echo "⚠️  gettext نصب نیست. در حال نصب..."
    sudo apt-get update
    sudo apt-get install -y gettext
fi

# 2. فعال‌سازی Virtual Environment
echo "🐍 فعال‌سازی Virtual Environment..."
source venv/bin/activate

# 3. کامپایل کردن فایل‌های ترجمه
echo "🔄 کامپایل فایل‌های ترجمه..."
python manage.py compilemessages

# 4. Restart سرور (اگر در development هستید)
echo ""
echo "✅ ترجمه‌ها بروزرسانی شدند!"
echo ""
echo "⚠️  یادآوری:"
echo "   - اگر در Production هستید، سرور را Restart کنید"
echo "   - مرورگر را Hard Refresh کنید (Ctrl+F5)"
echo ""
echo "🎉 تمام!"

