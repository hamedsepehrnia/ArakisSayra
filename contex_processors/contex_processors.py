from core.models import SiteInfo
from products.models import Category


def site_info(request):
    try:
        info = SiteInfo.objects.first()
        return {
            'phone_number1': info.phone_number1 if info else '',
            'phone_number2': info.phone_number2 if info else '',
            'phone_number3': info.phone_number3 if info else '',
            'address': info.address if info else '',
            'email': info.email if info else '',
            'about_text': info.about_text if info else '',
            'work_hour1': info.work_hour1 if info else '',
            'work_hour2': info.work_hour2 if info else '',
            'work_hour3': info.work_hour3 if info else '',
            'instagram_page': info.instagram_page if info else '',

        }
    except:
        return {
            'phone_number1': '',
            'phone_number2': '',
            'phone_number3': '',
            'address': '',
            'email': '',
            'about_text': '',

        }

def categories_context(request):
    categories = Category.objects.filter(parent__isnull=True, slug__isnull=False).exclude(slug='')
    return {
        "categories": categories
    }

