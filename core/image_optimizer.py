"""
بهینه‌سازی خودکار تصاویر آپلود شده
"""
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def optimize_image(image_field, max_size=(2000, 2000), quality=85, format='JPEG'):
    """
    بهینه‌سازی تصویر با کاهش حجم بدون افت کیفیت قابل توجه
    
    Args:
        image_field: فیلد ImageField
        max_size: حداکثر ابعاد (عرض، ارتفاع)
        quality: کیفیت فشرده‌سازی (1-100)
        format: فرمت خروجی (JPEG, PNG, WebP)
    
    Returns:
        InMemoryUploadedFile: تصویر بهینه شده
    """
    if not image_field:
        return None
    
    try:
        # باز کردن تصویر
        img = Image.open(image_field)
        
        # حفظ شفافیت برای PNG
        if img.mode in ('RGBA', 'LA', 'P'):
            if format == 'JPEG':
                # تبدیل RGBA به RGB برای JPEG
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            else:
                format = 'PNG'
        else:
            img = img.convert('RGB')
        
        # Resize اگر تصویر بزرگتر از حد مجاز باشد
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # ذخیره در buffer
        output = BytesIO()
        
        # تنظیمات بهینه‌سازی
        save_kwargs = {
            'format': format,
            'quality': quality,
            'optimize': True,
        }
        
        # تنظیمات اضافی برای JPEG
        if format == 'JPEG':
            save_kwargs['progressive'] = True
            save_kwargs['subsampling'] = 0  # بهترین کیفیت
        
        img.save(output, **save_kwargs)
        output.seek(0)
        
        # تعیین نام فایل و content type
        file_name = image_field.name.split('/')[-1]
        if '.' in file_name:
            file_name = '.'.join(file_name.split('.')[:-1])
        
        content_types = {
            'JPEG': 'image/jpeg',
            'PNG': 'image/png',
            'WebP': 'image/webp'
        }
        
        file_extension = format.lower() if format != 'JPEG' else 'jpg'
        new_file_name = f"{file_name}.{file_extension}"
        
        # ایجاد فایل جدید
        optimized_image = InMemoryUploadedFile(
            output,
            'ImageField',
            new_file_name,
            content_types.get(format, 'image/jpeg'),
            sys.getsizeof(output),
            None
        )
        
        return optimized_image
        
    except Exception as e:
        print(f"خطا در بهینه‌سازی تصویر: {str(e)}")
        return image_field


def optimize_banner_image(image_field):
    """
    بهینه‌سازی تصویر بنر
    سایز: 1920×960 | کیفیت: 85
    """
    return optimize_image(image_field, max_size=(1920, 960), quality=85)


def optimize_product_image(image_field):
    """
    بهینه‌سازی تصویر محصول
    سایز: 1000×1000 | کیفیت: 88
    """
    return optimize_image(image_field, max_size=(1000, 1000), quality=88)


def optimize_blog_image(image_field):
    """
    بهینه‌سازی تصویر بلاگ/خبر
    سایز: 900×585 | کیفیت: 85
    """
    return optimize_image(image_field, max_size=(900, 585), quality=85)


def optimize_about_image(image_field):
    """
    بهینه‌سازی تصویر درباره ما
    سایز: 800×600 | کیفیت: 85
    """
    return optimize_image(image_field, max_size=(800, 600), quality=85)

