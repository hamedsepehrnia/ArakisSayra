# Environment Variables Setup Guide

## Overview
This project uses environment variables to manage sensitive configuration data such as database credentials, secret keys, and other settings.

## Setup Instructions

### 1. Install Required Package
First, install the `python-decouple` package:

```bash
pip install -r requirements.txt
```

Or specifically:

```bash
pip install python-decouple
```

### 2. Create Your .env File
Copy the example file and edit it with your actual values:

```bash
cp .env.example .env
```

Then edit `.env` with your actual credentials:

```bash
nano .env  # or use your preferred editor
```

### 3. Environment Variables Explained

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for cryptographic signing | `django-insecure-xxx...` |
| `DEBUG` | Enable/disable debug mode | `False` (production), `True` (development) |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `example.com,www.example.com` |
| `DB_ENGINE` | Database engine backend | `django.db.backends.mysql` |
| `DB_NAME` | Database name | `arakissa_db` |
| `DB_USER` | Database username | `arakissa_user` |
| `DB_PASSWORD` | Database password | `YourSecurePassword` |
| `DB_HOST` | Database host address | `localhost` |
| `DB_PORT` | Database port | `3306` |
| `STATIC_ROOT` | Path for collected static files | `/home/user/public_html/static` |
| `MEDIA_ROOT` | Path for user uploaded files | `/home/user/public_html/media` |

### 4. Security Notes

⚠️ **IMPORTANT:**
- Never commit `.env` file to version control (it's already in `.gitignore`)
- Keep your `SECRET_KEY` and `DB_PASSWORD` secure
- Use different values for development and production
- Generate a new `SECRET_KEY` for production using:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5. Development vs Production

#### Development Setup:
```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
STATIC_ROOT=./staticfiles
MEDIA_ROOT=./media
```

#### Production Setup:
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
STATIC_ROOT=/home/user/public_html/static
MEDIA_ROOT=/home/user/public_html/media
```

### 6. Verify Setup

Test that your environment variables are loaded correctly:

```bash
python manage.py shell
```

Then in the shell:

```python
from django.conf import settings
print(settings.SECRET_KEY)
print(settings.DATABASES)
```

## Troubleshooting

### Error: "DB_PASSWORD not found in environment"
- Make sure your `.env` file exists in the project root
- Check that the variable name matches exactly (case-sensitive)
- Ensure there are no quotes around values in `.env`

### Error: "Incorrect string value"
- Check your database charset settings
- Uncomment the OPTIONS section in settings.py if using MySQL

## Support

For more information, see:
- [Python Decouple Documentation](https://github.com/HBNetwork/python-decouple)
- [Django Settings Documentation](https://docs.djangoproject.com/en/5.2/ref/settings/)

