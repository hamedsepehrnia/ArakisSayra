"""
Automatic optimization for uploaded images
"""
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def optimize_image(image_field, max_size=(2000, 2000), quality=85, format='JPEG'):
    """
    Optimize image by reducing file size without significant quality loss
    
    Args:
        image_field: Django ImageField instance
        max_size: Maximum dimensions (width, height)
        quality: Compression quality (1-100)
        format: Output format (JPEG, PNG, WebP)
    
    Returns:
        InMemoryUploadedFile: Optimized image
    """
    if not image_field:
        return None
    
    try:
        # Open image
        img = Image.open(image_field)
        
        # Preserve transparency for PNG
        if img.mode in ('RGBA', 'LA', 'P'):
            if format == 'JPEG':
                # Convert RGBA to RGB for JPEG
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            else:
                format = 'PNG'
        else:
            img = img.convert('RGB')
        
        # Resize if image is larger than max size
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Save to buffer
        output = BytesIO()
        
        # Optimization settings
        save_kwargs = {
            'format': format,
            'quality': quality,
            'optimize': True,
        }
        
        # Additional settings for JPEG
        if format == 'JPEG':
            save_kwargs['progressive'] = True
            save_kwargs['subsampling'] = 0  # Best quality
        
        img.save(output, **save_kwargs)
        output.seek(0)
        
        # Set file name and content type
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
        
        # Create new file
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
        print(f"Error optimizing image: {str(e)}")
        return image_field


def optimize_banner_image(image_field):
    """
    Optimize banner image
    Size: 1920×960 | Quality: 85
    """
    return optimize_image(image_field, max_size=(1920, 960), quality=85)


def optimize_product_image(image_field):
    """
    Optimize product image
    Size: 1000×1000 | Quality: 88
    """
    return optimize_image(image_field, max_size=(1000, 1000), quality=88)


def optimize_blog_image(image_field):
    """
    Optimize blog/news image
    Size: 900×585 | Quality: 85
    """
    return optimize_image(image_field, max_size=(900, 585), quality=85)


def optimize_about_image(image_field):
    """
    Optimize about us image
    Size: 800×600 | Quality: 85
    """
    return optimize_image(image_field, max_size=(800, 600), quality=85)

