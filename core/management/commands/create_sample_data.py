from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import SiteInfo, Banner
from products.models import Category, Product
from blog.models import Category as BlogCategory, Post, News
from slugify import slugify
import jdatetime
import random


class Command(BaseCommand):
    help = 'Create sample data for the website'

    def handle(self, *args, **options):
        # Create site information
        if not SiteInfo.objects.exists():
            SiteInfo.objects.create(
                phone_number1='031-32567890',
                phone_number2='09131234567',
                phone_number3='031-32567891',
                address_fa='اصفهان، شهرک صنعتی جی، خیابان یکم، فرعی ۱۴، پلاک ۱۹۵',
                address_en='Isfahan, J Industrial Town, First Street, 14th Alley, No. 195',
                email='info@arakissayra.ir',
                about_text_fa='مجتمع شیمیایی ماهان سپهر اصفهان، پیشگام در تولید مواد شیمیایی صنعتی از سال ۱۳۸۲، با برند شوینده آراکیس سایرا، کیفیت پایدار و سازگار با محیط زیست. ما با بهره‌گیری از فناوری‌های روز دنیا و تیمی متخصص، محصولاتی با کیفیت بالا تولید می‌کنیم که نیازهای صنایع مختلف را برآورده می‌سازد.',
                about_text_en='Mahan Sepehr Chemical Complex of Isfahan, a pioneer in the production of industrial chemicals since 2003, with the Arakis Sayra detergent brand, sustainable quality and environmentally friendly. We produce high-quality products using world-class technologies and a specialized team that meet the needs of various industries.',
                work_hour1_fa='شنبه تا چهارشنبه: ۸:۰۰ - ۱۷:۰۰',
                work_hour1_en='Saturday to Wednesday: 8:00 AM - 5:00 PM',
                work_hour2_fa='پنجشنبه: ۸:۰۰ - ۱۲:۰۰',
                work_hour2_en='Thursday: 8:00 AM - 12:00 PM',
                work_hour3_fa='جمعه: تعطیل',
                work_hour3_en='Friday: Closed',
                instagram_page='@arakissayra'
            )
            self.stdout.write(self.style.SUCCESS('✓ Site information created'))

        # Create product categories
        categories_data = [
            {'name_fa': 'شوینده‌های صنعتی', 'name_en': 'Industrial Detergents', 'slug': 'industrial-detergents'},
            {'name_fa': 'مواد شیمیایی صنعتی', 'name_en': 'Industrial Chemicals', 'slug': 'industrial-chemicals'},
            {'name_fa': 'پاک‌کننده‌های تخصصی', 'name_en': 'Specialty Cleaners', 'slug': 'specialty-cleaners'},
            {'name_fa': 'شوینده‌های خانگی', 'name_en': 'Household Detergents', 'slug': 'household-detergents'},
            {'name_fa': 'محصولات بهداشتی', 'name_en': 'Hygiene Products', 'slug': 'hygiene-products'},
            {'name_fa': 'محصولات خودرویی', 'name_en': 'Automotive Products', 'slug': 'automotive-products'},
        ]
        
        created_categories = []
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name_fa': cat_data['name_fa'], 'name_en': cat_data['name_en'], 'name': cat_data['name_fa']}
            )
            if created:
                created_categories.append(cat)
                self.stdout.write(f'✓ Category created: {cat.name_fa}')

        # Create subcategories
        if len(created_categories) >= 4:
            subcategories_data = [
                {'parent': created_categories[0], 'name_fa': 'صابون مایع صنعتی', 'name_en': 'Industrial Liquid Soap', 'slug': 'industrial-liquid-soap'},
                {'parent': created_categories[0], 'name_fa': 'شامپو فرش', 'name_en': 'Carpet Shampoo', 'slug': 'carpet-shampoo'},
                {'parent': created_categories[0], 'name_fa': 'پاک‌کننده چربی', 'name_en': 'Degreaser', 'slug': 'degreaser'},
                {'parent': created_categories[1], 'name_fa': 'اسیدها', 'name_en': 'Acids', 'slug': 'acids'},
                {'parent': created_categories[1], 'name_fa': 'قلیاها', 'name_en': 'Alkalis', 'slug': 'alkalis'},
                {'parent': created_categories[2], 'name_fa': 'پاک‌کننده شیشه', 'name_en': 'Glass Cleaner', 'slug': 'glass-cleaner'},
                {'parent': created_categories[3], 'name_fa': 'مایع ظرفشویی', 'name_en': 'Dishwashing Liquid', 'slug': 'dishwashing-liquid'},
            ]
            
            for subcat_data in subcategories_data:
                cat, created = Category.objects.get_or_create(
                    slug=subcat_data['slug'],
                    defaults={
                        'name_fa': subcat_data['name_fa'],
                        'name_en': subcat_data['name_en'],
                        'name': subcat_data['name_fa'],
                        'parent': subcat_data['parent']
                    }
                )
                if created:
                    self.stdout.write(f'✓ Subcategory created: {cat.name_fa}')

        # Create products
        products_data = [
            {
                'title_fa': 'شوینده صنعتی چندمنظوره آراکیس',
                'title_en': 'Arakis Multi-Purpose Industrial Detergent',
                'short_description_fa': 'شوینده قوی و مؤثر برای استفاده در صنایع مختلف',
                'short_description_en': 'Strong and effective detergent for use in various industries',
                'description_fa': 'شوینده صنعتی آراکیس یک محصول چندمنظوره است که می‌تواند در پاک‌سازی سطوح مختلف، از جمله فلزات، سرامیک، پلاستیک و چوب استفاده شود. این محصول با فرمولاسیون پیشرفته، لکه‌های سخت را به راحتی پاک می‌کند و بدون آسیب رساندن به سطح، تمیزی ماندگار ایجاد می‌کند.',
                'description_en': 'Arakis industrial detergent is a multi-purpose product that can be used to clean various surfaces, including metals, ceramics, plastics and wood. This product, with its advanced formulation, easily removes tough stains and creates lasting cleanliness without damaging the surface.',
                'size': 20,
                'container_type_fa': 'گالن',
                'container_type_en': 'Gallon',
                'attributes_fa': 'محلول در آب، بدون بو، دوستدار محیط زیست',
                'attributes_en': 'Water soluble, odorless, environmentally friendly',
                'category_slug': 'industrial-detergents'
            },
            {
                'title_fa': 'پاک‌کننده شیشه و آینه',
                'title_en': 'Glass and Mirror Cleaner',
                'short_description_fa': 'پاک‌کننده تخصصی برای شیشه و آینه',
                'short_description_en': 'Specialized cleaner for glass and mirrors',
                'description_fa': 'پاک‌کننده شیشه و آینه آراکیس با فرمول ویژه، بدون ایجاد رد و لکه، شیشه‌ها را به طور کامل پاک می‌کند. مناسب برای استفاده در خانه، اداره و صنایع مختلف. این محصول با ویژگی ضد مه، مانع از بخار گرفتن شیشه‌ها می‌شود.',
                'description_en': 'Arakis glass and mirror cleaner, with its special formula, cleans glasses completely without leaving streaks. Suitable for use at home, office and various industries. This product with anti-fog feature prevents fogging of glasses.',
                'size': 5,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'ضد مه، بدون اثر انگشت، پاک‌سازی سریع',
                'attributes_en': 'Anti-fog, no fingerprints, quick cleaning',
                'category_slug': 'glass-cleaner'
            },
            {
                'title_fa': 'شامپو فرش حرفه‌ای',
                'title_en': 'Professional Carpet Shampoo',
                'short_description_fa': 'شامپو تخصصی برای شستشوی فرش',
                'short_description_en': 'Specialized shampoo for carpet washing',
                'description_fa': 'شامپو فرش آراکیس با قدرت پاک‌کنندگی بالا، لکه‌های مختلف فرش را به راحتی از بین می‌برد. این محصول رنگی نیست و باعث تغییر رنگ فرش نمی‌شود. فرمولاسیون ملایم آن باعث حفظ بافت طبیعی فرش می‌شود.',
                'description_en': 'Arakis carpet shampoo with high cleaning power easily removes various carpet stains. This product is colorless and does not cause carpet discoloration. Its mild formulation preserves the natural texture of the carpet.',
                'size': 4,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'رنگی نیست، محافظ بافت فرش، ضد باکتری',
                'attributes_en': 'Colorless, carpet texture protector, antibacterial',
                'category_slug': 'carpet-shampoo'
            },
            {
                'title_fa': 'صابون مایع صنعتی',
                'title_en': 'Industrial Liquid Soap',
                'short_description_fa': 'صابون مایع برای استفاده در محیط‌های صنعتی',
                'short_description_en': 'Liquid soap for use in industrial environments',
                'description_fa': 'صابون مایع صنعتی آراکیس با قدرت کف‌زایی بالا و پاک‌کنندگی مؤثر، مناسب برای استفاده در کارخانجات، کارگاه‌ها و محیط‌های صنعتی است. این محصول پوست را نرم کرده و مانع از خشکی و ترک خوردگی دست می‌شود.',
                'description_en': 'Arakis industrial liquid soap with high foaming power and effective cleaning is suitable for use in factories, workshops and industrial environments. This product softens the skin and prevents hand dryness and cracking.',
                'size': 20,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'کف فراوان، ضد باکتری، مرطوب‌کننده پوست',
                'attributes_en': 'High foam, antibacterial, skin moisturizer',
                'category_slug': 'industrial-liquid-soap'
            },
            {
                'title_fa': 'پاک‌کننده چربی سینک',
                'title_en': 'Kitchen Sink Degreaser',
                'short_description_fa': 'پاک‌کننده قوی برای چربی‌های آشپزخانه',
                'short_description_en': 'Powerful cleaner for kitchen grease',
                'description_fa': 'این محصول به طور خاص برای پاک‌سازی چربی‌های سخت سینک، شیرآلات و کابینت‌های آشپزخانه طراحی شده است. با قدرت پاک‌کنندگی بالا و بدون خراش، سطوح استیل و کروم را درخشان می‌کند.',
                'description_en': 'This product is specifically designed to clean tough grease from sinks, faucets and kitchen cabinets. With high cleaning power and without scratching, it makes steel and chrome surfaces shine.',
                'size': 1,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'ضد چربی، ضد زنگ، درخشان‌کننده',
                'attributes_en': 'Degreaser, anti-rust, shine enhancer',
                'category_slug': 'household-detergents'
            },
            {
                'title_fa': 'پاک‌کننده سرویس بهداشتی',
                'title_en': 'Toilet Bowl Cleaner',
                'short_description_fa': 'پاک‌کننده تخصصی برای سرویس بهداشتی',
                'short_description_en': 'Specialized cleaner for toilets',
                'description_fa': 'پاک‌کننده سرویس بهداشتی آراکیس با قدرت ضدعفونی‌کنندگی و خوشبوکنندگی بالا، سرویس بهداشتی را کاملاً تمیز و بهداشتی می‌کند. این محصول لکه‌های آهکی و صابونی را به راحتی از بین می‌برد.',
                'description_en': 'Arakis toilet cleaner with high disinfecting and fragrancing power makes the toilet completely clean and hygienic. This product easily removes lime and soap stains.',
                'size': 2,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'ضد باکتری، ضد قارچ، خوشبوکننده',
                'attributes_en': 'Antibacterial, antifungal, air freshener',
                'category_slug': 'hygiene-products'
            },
            {
                'title_fa': 'شامپوی بدنه خودرو',
                'title_en': 'Car Body Shampoo',
                'short_description_fa': 'شامپوی مخصوص شستشوی خودرو',
                'short_description_en': 'Special car washing shampoo',
                'description_fa': 'شامپوی بدنه خودرو آراکیس با فرمولاسیون پیشرفته، رنگ خودرو را حفظ کرده و آن را براق می‌کند. این محصول کف فراوان دارد و بدون آسیب رساندن به رنگ، آلودگی‌ها را پاک می‌کند.',
                'description_en': 'Arakis car body shampoo with advanced formulation preserves the car paint and makes it shiny. This product has abundant foam and cleans pollutants without damaging the paint.',
                'size': 5,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'محافظ رنگ، کف فراوان، براق‌کننده',
                'attributes_en': 'Paint protector, high foam, shine enhancer',
                'category_slug': 'automotive-products'
            },
            {
                'title_fa': 'مایع ظرفشویی غلیظ',
                'title_en': 'Concentrated Dishwashing Liquid',
                'short_description_fa': 'مایع ظرفشویی با قدرت چربی‌زدایی بالا',
                'short_description_en': 'Dishwashing liquid with high degreasing power',
                'description_fa': 'مایع ظرفشویی آراکیس با فرمول غلیظ و قدرت چربی‌زدایی بالا، ظروف را به طور کامل تمیز می‌کند. این محصول کف پایدار دارد و ملایم با پوست دست است.',
                'description_en': 'Arakis dishwashing liquid with concentrated formula and high degreasing power cleans dishes completely. This product has stable foam and is gentle on hand skin.',
                'size': 4,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'غلیظ، کف پایدار، ملایم با پوست',
                'attributes_en': 'Concentrated, stable foam, gentle on skin',
                'category_slug': 'dishwashing-liquid'
            },
            {
                'title_fa': 'پاک‌کننده چندمنظوره خانگی',
                'title_en': 'Multipurpose Home Cleaner',
                'short_description_fa': 'پاک‌کننده چندمنظوره برای خانه',
                'short_description_en': 'Multipurpose cleaner for home',
                'description_fa': 'پاک‌کننده چندمنظوره آراکیس برای تمیز کردن سطوح مختلف خانه از جمله کف‌ها، کاشی‌ها، کابینت‌ها و ... مناسب است. این محصول خوشبو بوده و رد نمی‌گذارد.',
                'description_en': 'Arakis multipurpose cleaner is suitable for cleaning various home surfaces including floors, tiles, cabinets, etc. This product is fragrant and leaves no residue.',
                'size': 2,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'چندمنظوره، خوشبو، بدون رد',
                'attributes_en': 'Multipurpose, fragrant, no residue',
                'category_slug': 'household-detergents'
            },
            {
                'title_fa': 'وایتکس رنگی',
                'title_en': 'Color Bleach',
                'short_description_fa': 'سفیدکننده و ضدعفونی‌کننده',
                'short_description_en': 'Whitener and disinfectant',
                'description_fa': 'وایتکس رنگی آراکیس برای سفید کردن و ضدعفونی کردن لباس‌ها و سطوح مناسب است. این محصول با فرمول پیشرفته، رنگ پارچه را حفظ می‌کند.',
                'description_en': 'Arakis color bleach is suitable for whitening and disinfecting clothes and surfaces. This product with advanced formula preserves fabric color.',
                'size': 4,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'ضدعفونی‌کننده، محافظ رنگ، سفیدکننده',
                'attributes_en': 'Disinfectant, color protector, whitener',
                'category_slug': 'household-detergents'
            },
            {
                'title_fa': 'اسید کلریدریک صنعتی',
                'title_en': 'Industrial Hydrochloric Acid',
                'short_description_fa': 'اسید قوی برای پاک‌سازی صنعتی',
                'short_description_en': 'Strong acid for industrial cleaning',
                'description_fa': 'اسید کلریدریک صنعتی آراکیس برای پاک‌سازی سطوح سخت، رسوب‌زدایی و کارهای صنعتی استفاده می‌شود. استفاده از دستکش و ماسک الزامی است.',
                'description_en': 'Arakis industrial hydrochloric acid is used for cleaning hard surfaces, descaling and industrial work. Using gloves and mask is mandatory.',
                'size': 30,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'قدرت بالا، رسوب‌بر، حرفه‌ای',
                'attributes_en': 'High power, descaler, professional',
                'category_slug': 'acids'
            },
            {
                'title_fa': 'مایع چرم کفش',
                'title_en': 'Shoe Polish Liquid',
                'short_description_fa': 'تمیز‌کننده و براق‌کننده کفش',
                'short_description_en': 'Shoe cleaner and polisher',
                'description_fa': 'مایع چرم کفش آراکیس برای تمیز کردن و براق کردن کفش‌های چرمی استفاده می‌شود. این محصول چرم را نرم و انعطاف‌پذیر نگه می‌دارد.',
                'description_en': 'Arakis shoe polish liquid is used to clean and polish leather shoes. This product keeps leather soft and flexible.',
                'size': 1,
                'container_type_fa': 'لیتر',
                'container_type_en': 'Liter',
                'attributes_fa': 'براق‌کننده، نرم‌کننده چرم، محافظ',
                'attributes_en': 'Polisher, leather softener, protector',
                'category_slug': 'specialty-cleaners'
            },
        ]

        for product_data in products_data:
            category = Category.objects.filter(slug=product_data['category_slug']).first()
            if category:
                product_dict = {
                    'title_fa': product_data['title_fa'],
                    'title_en': product_data['title_en'],
                    'title': product_data['title_fa'],
                    'short_description_fa': product_data['short_description_fa'],
                    'short_description_en': product_data['short_description_en'],
                    'short_description': product_data['short_description_fa'],
                    'description_fa': product_data['description_fa'],
                    'description_en': product_data['description_en'],
                    'description': product_data['description_fa'],
                    'size': product_data['size'],
                    'container_type_fa': product_data['container_type_fa'],
                    'container_type_en': product_data['container_type_en'],
                    'container_type': product_data['container_type_fa'],
                    'attributes_fa': product_data['attributes_fa'],
                    'attributes_en': product_data['attributes_en'],
                    'attributes': product_data['attributes_fa'],
                    'category': category
                }
                product, created = Product.objects.get_or_create(
                    slug=slugify(product_data['title_fa']),
                    defaults=product_dict
                )
                if created:
                    self.stdout.write(f'✓ Product created: {product.title_fa}')

        # Create blog categories
        blog_categories_data = [
            'اخبار',
            'مقالات',
            'راهنمای استفاده',
            'تکنولوژی',
            'محیط زیست',
            'ایمنی',
            'صنعت شیمیایی',
        ]
        
        for cat_name in blog_categories_data:
            cat, created = BlogCategory.objects.get_or_create(name=cat_name)
            if created:
                self.stdout.write(f'✓ Blog category created: {cat.name}')

        # Create blog posts
        if not User.objects.exists():
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@arakissayra.ir',
                password='admin123'
            )
        else:
            admin_user = User.objects.first()

        posts_data = [
            {
                'title': 'نکات مهم در استفاده از شوینده‌های صنعتی',
                'content': '''در استفاده از شوینده‌های صنعتی، رعایت نکات ایمنی بسیار مهم است. همیشه از دستکش و ماسک استفاده کنید و فضای کار را تهویه کنید. برای استفاده صحیح، رقیق‌سازی محصول مطابق با دستورالعمل روی بسته‌بندی انجام دهید. از ترکیب چند ماده شوینده به طور همزمان خودداری کنید.

نکته مهم: همیشه مقدار کم را ابتدا تست کنید و در صورت عدم واکنش آلرژیک، استفاده کنید. بعد از اتمام کار، دست‌ها را با آب و صابون به خوبی بشویید.

اگر علائمی مانند قرمزی، سوزش یا خارش مشاهده کردید، فوراً استفاده را متوقف کرده و به پزشک مراجعه کنید.''',
                'categories': ['راهنمای استفاده', 'ایمنی']
            },
            {
                'title': 'راهکارهای کاهش مصرف آب در شستشو',
                'content': '''صرفه‌جویی در مصرف آب یکی از مهم‌ترین مسائل زیست‌محیطی است. با استفاده از شوینده‌های با کیفیت، می‌توانید آب کمتری مصرف کنید. استفاده از شوینده‌های غلیظ و مؤثر، نیاز به شستشوی مجدد را کاهش می‌دهد.

برای شستشوی خودرو، استفاده از سطل آب بهتر از شیلنگ است. برای شستشوی فرش، استفاده از دستگاه اسپری موثرتر از روش‌های قدیمی است.

با رعایت این نکات، می‌توانید تا ۳۰ درصد در مصرف آب صرفه‌جویی کنید و در عین حال، نتیجه بهتری دریافت کنید.''',
                'categories': ['محیط زیست', 'مقالات']
            },
            {
                'title': 'تکنولوژی جدید در تولید مواد شوینده',
                'content': '''صنعت تولید مواد شوینده در حال پیشرفت مداوم است. استفاده از نانو ذرات در فرمولاسیون شوینده‌ها، قدرت پاک‌کنندگی را افزایش داده است. این تکنولوژی باعث می‌شود که شوینده‌ها حتی در دمای پایین و آب سخت نیز به خوبی عمل کنند.

علاوه بر این، استفاده از مواد طبیعی و تجدیدپذیر در تولید شوینده‌ها، آسیب زیست‌محیطی را کاهش داده است. بسیاری از تولیدکنندگان پیشرو، به سمت استفاده از مواد زیستی حرکت کرده‌اند.

در آینده شاهد شوینده‌های هوشمندی خواهیم بود که با توجه به نوع لکه و سطح، خود را تنظیم می‌کنند.''',
                'categories': ['تکنولوژی', 'مقالات']
            },
            {
                'title': 'راهنمای انتخاب شوینده مناسب',
                'content': '''انتخاب شوینده مناسب برای هر سطح و نوع لکه بسیار مهم است. برای سطوح ظریف مانند شیشه و آینه، باید از شوینده‌های ملایم استفاده کنید. برای لکه‌های چربی، شوینده‌های قلیایی مناسب‌ترند.

نکته مهم: همیشه برچسب محصول را بخوانید و دستورالعمل استفاده را رعایت کنید. اگر مطمئن نیستید، ابتدا روی بخش کوچکی تست کنید.

برای سطوح فلزی، از شوینده‌های ضد زنگ استفاده کنید. برای سطوح چوبی، شوینده‌های خنثی بهترین گزینه هستند.''',
                'categories': ['راهنمای استفاده']
            },
            {
                'title': 'شوینده‌های سازگار با محیط زیست',
                'content': '''در دهه‌های اخیر، استفاده از شوینده‌های سازگار با محیط زیست به یک ضرورت تبدیل شده است. این محصولات با استفاده از مواد تجدیدپذیر و بیولوژیکی تولید می‌شوند و به راحتی در طبیعت تجزیه می‌شوند.

مزایای استفاده از شوینده‌های سبز شامل کاهش آلودگی آب، کاهش اثرات منفی بر حیات دریایی و سلامت بهتر برای خانواده شماست. این محصولات معمولاً هیچ ماده شیمیایی سمی ندارند.

شرکت آراکیس سایرا با تولید محصولات دوستدار محیط زیست، سهم خود را در حفظ طبیعت ایفا می‌کند.''',
                'categories': ['محیط زیست', 'مقالات']
            },
            {
                'title': 'صنعت شیمیایی و نقش آن در زندگی روزمره',
                'content': '''صنعت شیمیایی یکی از مهم‌ترین صنایع در جهان است که نقش کلیدی در زندگی روزمره ما دارد. از مواد شوینده گرفته تا داروها و کودهای کشاورزی، همه محصول این صنعت هستند.

در ایران، صنعت شیمیایی به طور مستمر در حال رشد است و شرکت‌های پیشرو مانند آراکیس سایرا با تولید محصولات با کیفیت، به توسعه این صنعت کمک می‌کنند.

استانداردهای بین‌المللی و رعایت اصول کیفیت، از مهم‌ترین عوامل موفقیت در این صنعت هستند.''',
                'categories': ['صنعت شیمیایی', 'مقالات']
            },
            {
                'title': 'ایمنی در استفاده از مواد شیمیایی خانگی',
                'content': '''استفاده صحیح از مواد شیمیایی خانگی می‌تواند از بسیاری از حوادث جلوگیری کند. همیشه مواد شیمیایی را در جای خشک و دور از دسترس کودکان نگهداری کنید. هرگز مواد شیمیایی را در بطری‌های نوشابه یا آب ریخته نکنید.

در هنگام استفاده، حتماً برچسب محصول را بخوانید و دستورالعمل‌های روی بسته را رعایت کنید. از ترکیب مواد مختلف خودداری کنید چون ممکن است واکنش خطرناکی رخ دهد.

در صورت تماس با پوست یا چشم، فوراً با آب فراوان بشویید و در صورت لزوم به پزشک مراجعه کنید.''',
                'categories': ['ایمنی', 'راهنمای استفاده']
            },
            {
                'title': 'نحوه صحیح نگهداری از محصولات شوینده',
                'content': '''نگهداری صحیح از محصولات شوینده، عمر مفید آن‌ها را افزایش می‌دهد و از خطرات احتمالی جلوگیری می‌کند. همیشه محصولات را در بسته‌بندی اصلی خود نگهداری کنید و در آب و هوای خنک و خشک قرار دهید.

از قرار دادن محصولات شوینده در معرض نور مستقیم آفتاب یا حرارت بالا خودداری کنید. همچنین آن‌ها را دور از مواد غذایی و دور از دسترس کودکان و حیوانات خانگی نگهداری کنید.

توجه به تاریخ انقضا نیز مهم است. استفاده از محصولات منقضی شده ممکن است اثربخشی کمتری داشته باشند.''',
                'categories': ['ایمنی', 'راهنمای استفاده']
            },
            {
                'title': 'تکنیک‌های پیشرفته تمیزکاری صنعتی',
                'content': '''تمیزکاری صنعتی نیازمند دانش و تجربه است. استفاده از دستگاه‌های مدرن مانند واترجت، اسکرابر و اسپری‌های فشار قوی، کار را سریع‌تر و موثرتر می‌کند.

در صنایع غذایی و دارویی، رعایت استانداردهای بهداشتی از اهمیت ویژه‌ای برخوردار است. استفاده از شوینده‌های مخصوص این صنایع که دارای تاییدیه‌های لازم هستند، ضروری است.

آموزش کارکنان در استفاده صحیح از محصولات شوینده و دستگاه‌های تمیزکاری، یکی از مهم‌ترین عوامل موفقیت در این حوزه است.''',
                'categories': ['صنعت شیمیایی', 'راهنمای استفاده']
            },
            {
                'title': 'آینده صنعت شوینده‌های سبز',
                'content': '''صنعت شوینده‌های سبز در حال رشد سریع است. پیش‌بینی می‌شود که تا سال ۲۰۳۰، بیش از ۵۰ درصد بازار شوینده‌ها به محصولات سازگار با محیط زیست اختصاص یابد.

شرکت‌های پیشرو در حال سرمایه‌گذاری روی تحقیق و توسعه محصولات سبز هستند. استفاده از انرژی‌های تجدیدپذیر در فرآیند تولید و کاهش مصرف آب، از دیگر اقدامات این شرکت‌ها است.

مصرف‌کنندگان نیز به طور فزاینده‌ای به دنبال محصولات سازگار با محیط زیست هستند و حاضرند برای آن‌ها هزینه بیشتری بپردازند.''',
                'categories': ['محیط زیست', 'تکنولوژی']
            },
        ]

        for post_data in posts_data:
            categories = [BlogCategory.objects.get(name=c) for c in post_data['categories']]
            # Create random dates for posts
            days_ago = random.randint(1, 60)
            post_date = jdatetime.date.today() - jdatetime.timedelta(days=days_ago)
            
            post, created = Post.objects.get_or_create(
                slug=slugify(post_data['title']),
                defaults={
                    'title': post_data['title'],
                    'content': post_data['content'],
                    'author': admin_user,
                    'created_date': post_date,
                    'created_time': jdatetime.datetime.now().time()
                }
            )
            if created:
                post.category.set(categories)
                self.stdout.write(f'✓ Post created: {post.title}')

        # Create news
        news_data = [
            {
                'title': 'رونمایی از محصول جدید آراکیس سایرا',
                'content': '''مجتمع شیمیایی ماهان سپهر اصفهان، محصول جدید خود را با نام "شوینده چندمنظوره آراکیس" معرفی کرد. این محصول با فرمولاسیون پیشرفته، برای استفاده در صنایع مختلف مناسب است.

مهندس مدیری، مدیر تولید این شرکت، در مراسم رونمایی گفت: «این محصول نتیجه سه سال تحقیق و توسعه است و با استانداردهای بین‌المللی تولید شده است.»

توزیع این محصول از هفته آینده آغاز می‌شود و در فروشگاه‌ها و سایت رسمی شرکت در دسترس خواهد بود.''',
            },
            {
                'title': 'شرکت آراکیس سایرا گواهینامه ISO دریافت کرد',
                'content': '''مجتمع شیمیایی ماهان سپهر اصفهان موفق به دریافت گواهینامه ISO 9001:2015 شد. این گواهینامه نشان‌دهنده کیفیت بالا در مدیریت و تولید محصولات شرکت است.

دکتر احمدی، مدیر کیفیت شرکت، در این رابطه گفت: «این گواهینامه نتیجه تلاش همکاران ما در تمام بخش‌هاست و نشان‌دهنده تعهد ما به کیفیت و رضایت مشتری است.»

با دریافت این گواهینامه، شرکت آراکیس سایرا آماده صادرات محصولات خود به کشورهای همسایه است.''',
            },
            {
                'title': 'نشست هم‌آفرینی با مشتریان آراکیس سایرا',
                'content': '''شرکت آراکیس سایرا با برگزاری نشست هم‌آفرینی، نظرات و پیشنهادات مشتریان خود را دریافت کرد. در این نشست، حدود ۱۰۰ مشتری از صنایع مختلف حضور داشتند.

مشتریان در خصوص بهبود کیفیت محصولات، تنوع بیشتر در بسته‌بندی و خدمات پس از فروش، پیشنهادات ارزشمندی ارائه دادند. شرکت متعهد شد که این پیشنهادات را در برنامه‌های آتی خود لحاظ کند.

به گفته مدیر فروش شرکت، این نشست‌ها به صورت دوره‌ای ادامه خواهد یافت و نقش مهمی در بهبود کیفیت خدمات خواهد داشت.''',
            },
            {
                'title': 'افتتاح خط تولید جدید در کارخانه آراکیس',
                'content': '''شرکت آراکیس سایرا با سرمایه‌گذاری ۱۵ میلیارد تومانی، خط تولید جدید خود را افتتاح کرد. این خط تولید با ظرفیت ۱۰۰ تن در ماه، به تولید محصولات با کیفیت بالاتر کمک می‌کند.

مدیرعامل شرکت در مراسم افتتاح گفت: «این سرمایه‌گذاری نشان از اعتماد ما به آینده صنعت شیمیایی کشور دارد. با این خط تولید، قادر خواهیم بود محصولات بیشتری را با کیفیت بهتر به بازار عرضه کنیم.»

این خط تولید با استفاده از فناوری‌های روز دنیا و با رعایت استانداردهای زیست‌محیطی راه‌اندازی شده است.''',
            },
            {
                'title': 'آراکیس سایرا، حامی تیم ملی والیبال ایران',
                'content': '''شرکت آراکیس سایرا به عنوان حامی رسمی تیم ملی والیبال ایران انتخاب شد. این همکاری برای مدت دو سال خواهد بود و شامل حمایت مالی و تدارکاتی می‌شود.

مدیر بازاریابی شرکت گفت: «حمایت از ورزش و ورزشکاران بخشی از مسئولیت اجتماعی ماست. امیدواریم این همکاری به موفقیت تیم ملی کمک کند.»

تیم ملی والیبال نیز از این حمایت استقبال کرد و قول داد که بهترین عملکرد را در مسابقات بین‌المللی ارائه دهد.''',
            },
            {
                'title': 'برگزاری کارگاه آموزشی رایگان استفاده از مواد شوینده',
                'content': '''شرکت آراکیس سایرا کارگاه آموزشی رایگان با موضوع «استفاده صحیح و ایمن از مواد شوینده» را برگزار کرد. در این کارگاه، بیش از ۲۰۰ نفر از خانم‌های خانه‌دار و کارکنان شرکت‌های خدماتی شرکت کردند.

کارشناسان شرکت در این کارگاه، نکات مهم در خصوص انتخاب، نگهداری و استفاده از مواد شوینده را آموزش دادند. همچنین در خصوص خطرات ترکیب مواد شیمیایی و اقدامات اولیه در صورت بروز حادثه توضیحاتی ارائه شد.

این کارگاه‌ها به صورت ماهانه ادامه خواهد داشت و علاقه‌مندان می‌توانند از طریق سایت شرکت ثبت نام کنند.''',
            },
            {
                'title': 'آراکیس سایرا در نمایشگاه بین‌المللی صنعت شیمیایی',
                'content': '''شرکت آراکیس سایرا در دهمین نمایشگاه بین‌المللی صنعت شیمیایی که در محل دائمی نمایشگاه‌های تهران برگزار شد، حضور پررنگی داشت.

در این نمایشگاه، محصولات جدید شرکت معرفی شد و قراردادهای همکاری با چندین شرکت داخلی و خارجی امضا شد. غرفه آراکیس سایرا با استقبال گسترده بازدیدکنندگان روبرو شد.

مدیرعامل شرکت گفت: «این نمایشگاه فرصت خوبی برای معرفی توانمندی‌های ما و آشنایی با نیازهای بازار بود. امیدواریم بتوانیم در سال‌های آینده نیز حضور فعال‌تری داشته باشیم.»''',
            },
            {
                'title': 'راه‌اندازی فروشگاه آنلاین آراکیس سایرا',
                'content': '''شرکت آراکیس سایرا فروشگاه اینترنتی خود را با آدرس shop.arakissayra.ir راه‌اندازی کرد. مشتریان اکنون می‌توانند محصولات شرکت را به صورت آنلاین خریداری کنند.

این فروشگاه امکانات متنوعی از جمله پرداخت آنلاین، ارسال رایگان برای خریدهای بالای ۵۰۰ هزار تومان و مشاوره رایگان را ارائه می‌دهد.

مدیر فروش شرکت گفت: «با توجه به رشد فروش آنلاین، تصمیم گرفتیم این کانال را نیز به کانال‌های فروش خود اضافه کنیم. مشتریان می‌توانند راحت‌تر و سریع‌تر خرید کنند.»''',
            },
            {
                'title': 'آراکیس سایرا، برنده جایزه بهترین کیفیت سال',
                'content': '''شرکت آراکیس سایرا در مراسم اختتامیه اولین جشنواره ملی کیفیت محصولات شیمیایی، عنوان «بهترین کیفیت سال» را کسب کرد.

این جایزه بر اساس نظرسنجی از مشتریان، ارزیابی محصولات توسط آزمایشگاه‌های مستقل و رعایت استانداردهای کیفیت اهدا شد.

مدیرعامل شرکت در مراسم دریافت جایزه گفت: «این افتخار نتیجه تلاش همه همکاران ماست. ما همواره سعی کرده‌ایم بهترین محصولات را به مشتریان خود ارائه دهیم و این جایزه نشان می‌دهد که در مسیر درستی حرکت می‌کنیم.»''',
            },
            {
                'title': 'امضای تفاهم‌نامه همکاری با دانشگاه صنعتی اصفهان',
                'content': '''شرکت آراکیس سایرا با دانشگاه صنعتی اصفهان تفاهم‌نامه همکاری امضا کرد. بر اساس این تفاهم‌نامه، دانشجویان رشته شیمی می‌توانند در کارخانه شرکت کارآموزی کنند.

همچنین شرکت از پروژه‌های تحقیقاتی دانشجویان حمایت خواهد کرد و در صورت موفقیت، نتایج را در خط تولید به کار خواهد گرفت.

رئیس دانشگاه گفت: «این همکاری برای دانشجویان ما فرصت بسیار خوبی است تا با دنیای واقعی صنعت آشنا شوند. امیدواریم این همکاری به توسعه صنعت شیمیایی کشور کمک کند.»''',
            },
            {
                'title': 'کمک ۵ میلیاردی آراکیس به مناطق سیل‌زده',
                'content': '''شرکت آراکیس سایرا به مناطق سیل‌زده جنوب کشور کمک ۵ میلیارد تومانی کرد. این کمک شامل مواد شوینده، بهداشتی و کمک‌های نقدی بود.

کامیون‌های حامل کمک‌های شرکت، دیروز به مناطق آسیب‌دیده رسیدند و در اختیار مسئولان قرار گرفتند.

مدیرعامل شرکت گفت: «در شرایط سخت، کمک به هموطنان وظیفه همه ماست. امیدواریم این کمک‌ها بتواند تا حدی به کاهش مشکلات مردم این مناطق کمک کند.»''',
            },
            {
                'title': 'صادرات محصولات آراکیس به عراق و افغانستان',
                'content': '''شرکت آراکیس سایرا موفق شد قراردادهای صادراتی با شرکت‌های عراقی و افغانستانی امضا کند. بر اساس این قراردادها، ماهانه ۵۰ تن از محصولات شرکت به این کشورها صادر می‌شود.

مدیر صادرات شرکت گفت: «بازارهای منطقه‌ای برای ما بسیار مهم هستند. محصولات ما از کیفیت بالایی برخوردار است و می‌تواند در رقابت با محصولات خارجی موفق باشد.»

این اولین گام شرکت برای ورود به بازارهای بین‌المللی است و قرار است در آینده به کشورهای دیگر نیز صادرات انجام شود.''',
            },
        ]

        for news_data_item in news_data:
            # Create random dates for news
            days_ago = random.randint(1, 90)
            news_date = jdatetime.date.today() - jdatetime.timedelta(days=days_ago)
            
            news, created = News.objects.get_or_create(
                slug=slugify(news_data_item['title']),
                defaults={
                    **news_data_item,
                    'created_date': news_date,
                    'created_time': jdatetime.datetime.now().time()
                }
            )
            if created:
                self.stdout.write(f'✓ News created: {news.title}')

        self.stdout.write(self.style.SUCCESS('\n✓✓✓ All sample data created successfully ✓✓✓'))



