from django.contrib import admin

from core.models import SiteInfo, Message, Banner
from mptt.admin import DraggableMPTTAdmin

from products.models import Product

admin.site.register(SiteInfo)
admin.site.register(Message)
admin.site.register(Banner)
from django.contrib import admin

admin.site.site_header = "مدیریت سایت"
admin.site.site_title = "پنل مدیریت"
admin.site.index_title = "به بخش مدیریت خوش آمدید"
