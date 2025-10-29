from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import SiteInfo, Banner
from products.models import Category, Product
from blog.models import Category as BlogCategory, Post, News
from slugify import slugify
import jdatetime


class Command(BaseCommand):
    help = 'ایجاد داده‌های نمونه برای سایت'

    def handle(self, *args, **options):
        # ایجاد اطلاعات سایت
        if not SiteInfo.objects.exists():
            SiteInfo.objects.create(
                phone_number1='031-32567890',
                phone_number2='09131234567',
                phone_number3='031-32567891',
                address='اصفهان، شهرک صنعتی جی، خیابان یکم، فرعی ۱۴، پلاک ۱۹۵',
                email='info@arakissayra.ir',
                about_text='مجتمع شیمیایی ماهان سپهر اصفهان، پیشگام در تولید مواد شیمیایی صنعتی از سال ۱۳۸۲، با برند شوینده آراکیس سایرا، کیفیت پایدار و سازگار با محیط زیست',
                work_hour1='شنبه تا چهارشنبه: ۸:۰۰ - ۱۷:۰۰',
                work_hour2='پنجشنبه: ۸:۰۰ - ۱۲:۰۰',
                work_hour3='جمعه: تعطیل',
                instagram_page='@arakissayra'
            )
            self.stdout.write(self.style.SUCCESS('اطلاعات سایت ایجاد شد'))

        # ایجاد دسته‌بندی‌های محصولات
        categories_data = [
            {'name': 'شوینده‌های صنعتی', 'slug': 'industrial-detergents'},
            {'name': 'مواد شیمیایی صنعتی', 'slug': 'industrial-chemicals'},
            {'name': 'پاک‌کننده‌های تخصصی', 'slug': 'specialty-cleaners'},
            {'name': 'شوینده‌های خانگی', 'slug': 'household-detergents'},
        ]
        
        created_categories = []
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
            if created:
                created_categories.append(cat)
                self.stdout.write(f'✓ دسته‌بندی ایجاد شد: {cat.name}')

        # ایجاد زیردسته‌ها
        if created_categories:
            subcategories_data = [
                {'parent': created_categories[0], 'name': 'صابون مایع صنعتی', 'slug': 'industrial-liquid-soap'},
                {'parent': created_categories[0], 'name': 'شامپو فرش', 'slug': 'carpet-shampoo'},
                {'parent': created_categories[1], 'name': 'اسیدها', 'slug': 'acids'},
                {'parent': created_categories[1], 'name': 'قلیاها', 'slug': 'alkalis'},
            ]
            
            for subcat_data in subcategories_data:
                cat, created = Category.objects.get_or_create(
                    slug=subcat_data['slug'],
                    defaults={
                        'name': subcat_data['name'],
                        'parent': subcat_data['parent']
                    }
                )
                if created:
                    self.stdout.write(f'✓ زیردسته ایجاد شد: {cat.name}')

        # ایجاد محصولات
        products_data = [
            {
                'title': 'شوینده صنعتی چندمنظوره آراکیس',
                'short_description': 'شوینده قوی و مؤثر برای استفاده در صنایع مختلف',
                'description': 'شوینده صنعتی آراکیس یک محصول چندمنظوره است که می‌تواند در پاک‌سازی سطوح مختلف، از جمله فلزات، سرامیک، پلاستیک و چوب استفاده شود. این محصول با فرمولاسیون پیشرفته، لکه‌های سخت را به راحتی پاک می‌کند و بدون آسیب رساندن به سطح، تمیزی ماندگار ایجاد می‌کند.',
                'size': 20,
                'container_type': 'گالن',
                'attributes': 'محلول در آب، بدون بو، دوستدار محیط زیست',
                'category_slug': 'industrial-detergents'
            },
            {
                'title': 'پاک‌کننده شیشه و آینه',
                'short_description': 'پاک‌کننده تخصصی برای شیشه و آینه',
                'description': 'پاک‌کننده شیشه و آینه آراکیس با فرمول ویژه، بدون ایجاد رد و لکه، شیشه‌ها را به طور کامل پاک می‌کند. مناسب برای استفاده در خانه، اداره و صنایع مختلف. این محصول با ویژگی ضد مه، مانع از بخار گرفتن شیشه‌ها می‌شود.',
                'size': 5,
                'container_type': 'لیتر',
                'attributes': 'ضد مه، بدون اثر انگشت، پاک‌سازی سریع',
                'category_slug': 'specialty-cleaners'
            },
            {
                'title': 'شامپو فرش حرفه‌ای',
                'short_description': 'شامپو تخصصی برای شستشوی فرش',
                'description': 'شامپو فرش آراکیس با قدرت پاک‌کنندگی بالا، لکه‌های مختلف فرش را به راحتی از بین می‌برد. این محصول رنگی نیست و باعث تغییر رنگ فرش نمی‌شود. فرمولاسیون ملایم آن باعث حفظ بافت طبیعی فرش می‌شود.',
                'size': 4,
                'container_type': 'لیتر',
                'attributes': 'رنگی نیست، محافظ بافت فرش، ضد باکتری',
                'category_slug': 'industrial-liquid-soap'
            },
            {
                'title': 'صابون مایع صنعتی',
                'short_description': 'صابون مایع برای استفاده در محیط‌های صنعتی',
                'description': 'صابون مایع صنعتی آراکیس با قدرت کف‌زایی بالا و پاک‌کنندگی مؤثر، مناسب برای استفاده در کارخانجات، کارگاه‌ها و محیط‌های صنعتی است. این محصول پوست را نرم کرده و مانع از خشکی و ترک خوردگی دست می‌شود.',
                'size': 20,
                'container_type': 'لیتر',
                'attributes': 'کف فراوان، ضد باکتری، مرطوب‌کننده پوست',
                'category_slug': 'industrial-liquid-soap'
            },
            {
                'title': 'پاک‌کننده چربی سینک آشپزخانه',
                'short_description': 'پاک‌کننده قوی برای چربی‌های آشپزخانه',
                'description': 'این محصول به طور خاص برای پاک‌سازی چربی‌های سخت سینک، شیرآلات و کابینت‌های آشپزخانه طراحی شده است. با قدرت پاک‌کنندگی بالا و بدون خراش، سطوح استیل و کروم را درخشان می‌کند.',
                'size': 1,
                'container_type': 'لیتر',
                'attributes': 'ضد چربی، ضد زنگ، درخشان‌کننده',
                'category_slug': 'household-detergents'
            },
            {
                'title': 'پاک‌کننده سرویس بهداشتی',
                'short_description': 'پاک‌کننده تخصصی برای سرویس بهداشتی',
                'description': 'پاک‌کننده سرویس بهداشتی آراکیس با قدرت ضدعفونی‌کنندگی و خوشبوکنندگی بالا، سرویس بهداشتی را کاملاً تمیز و بهداشتی می‌کند. این محصول لکه‌های آهکی و صابونی را به راحتی از بین می‌برد.',
                'size': 2,
                'container_type': 'لیتر',
                'attributes': 'ضد باکتری، ضد قارچ، خوشبوکننده',
                'category_slug': 'specialty-cleaners'
            },
        ]

        for product_data in products_data:
            category = Category.objects.filter(slug=product_data['category_slug']).first()
            if category:
                product, created = Product.objects.get_or_create(
                    slug=slugify(product_data['title']),
                    defaults={**{k: v for k, v in product_data.items() if k != 'category_slug'}, 'category': category}
                )
                if created:
                    self.stdout.write(f'✓ محصول ایجاد شد: {product.title}')

        # ایجاد دسته‌بندی‌های بلاگ
        blog_categories_data = [
            'اخبار',
            'مقالات',
            'راهنمای استفاده',
            'تکنولوژی',
        ]
        
        for cat_name in blog_categories_data:
            cat, created = BlogCategory.objects.get_or_create(name=cat_name)
            if created:
                self.stdout.write(f'✓ دسته‌بندی بلاگ ایجاد شد: {cat.name}')

        # ایجاد پست‌های بلاگ
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
                'categories': ['راهنمای استفاده', 'مقالات']
            },
            {
                'title': 'راهکارهای کاهش مصرف آب در شستشو',
                'content': '''صرفه‌جویی در مصرف آب یکی از مهم‌ترین مسائل زیست‌محیطی است. با استفاده از شوینده‌های با کیفیت، می‌توانید آب کمتری مصرف کنید. استفاده از شوینده‌های غلیظ و مؤثر، نیاز به شستشوی مجدد را کاهش می‌دهد.

برای شستشوی خودرو، استفاده از سطل آب بهتر از شیلنگ است. برای شستشوی فرش، استفاده از دستگاه اسپری موثرتر از روش‌های قدیمی است.

با رعایت این نکات، می‌توانید تا ۳۰ درصد در مصرف آب صرفه‌جویی کنید و در عین حال، نتیجه بهتری دریافت کنید.''',
                'categories': ['راهنمای استفاده', 'مقالات']
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
        ]

        for post_data in posts_data:
            categories = [BlogCategory.objects.get(name=c) for c in post_data['categories']]
            post, created = Post.objects.get_or_create(
                slug=slugify(post_data['title']),
                defaults={
                    'title': post_data['title'],
                    'content': post_data['content'],
                    'author': admin_user,
                    'created_date': jdatetime.date.today(),
                    'created_time': jdatetime.datetime.now().time()
                }
            )
            if created:
                post.category.set(categories)
                self.stdout.write(f'✓ پست ایجاد شد: {post.title}')

        # ایجاد اخبار
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
        ]

        for news_data_item in news_data:
            news, created = News.objects.get_or_create(
                slug=slugify(news_data_item['title']),
                defaults={
                    **news_data_item,
                    'created_date': jdatetime.date.today(),
                    'created_time': jdatetime.datetime.now().time()
                }
            )
            if created:
                self.stdout.write(f'✓ خبر ایجاد شد: {news.title}')

        self.stdout.write(self.style.SUCCESS('\n✓✓✓ تمام داده‌های نمونه با موفقیت ایجاد شدند ✓✓✓'))

