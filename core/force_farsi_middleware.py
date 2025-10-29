# from django.shortcuts import redirect

# class ForceFarsiMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # فقط اگر هیچ کوکی زبان وجود ندارد و مسیر بدون زبان است
#         if (
#             not request.COOKIES.get('django_language')
#             and request.path == '/'
#         ):
#             return redirect('/fa/')
#         return self.get_response(request) 