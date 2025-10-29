from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/<slug:slug>', views.news_details, name='news_details'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_post'),

]
