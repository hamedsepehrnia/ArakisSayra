from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Post, Category, News


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 10
    ordering = ['-created_date', '-created_time']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_categories'] = Category.objects.all()
        context['latest_three_posts'] = Post.objects.order_by('-created_date', '-created_time')[:3]
        return context

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blog-post.html', {'post': post})


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 10
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=category).order_by('-created_date', '-created_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_categories'] = Category.objects.all()
        context['latest_three_posts'] = Post.objects.order_by('-created_date', '-created_time')[:3]
        return context

class NewsListView(ListView):
    model = News
    template_name = 'blog/news.html'
    paginate_by = 10
    ordering = ['-created_date', '-created_time']

    def get_queryset(self):
        # Main query for paginated news list
        return News.objects.order_by('-created_date', '-created_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Latest three news for slider
        context['latest_three_news'] = News.objects.order_by('-created_date', '-created_time')[:3]
        return context


def news_details(request, slug):
    news = News.objects.get(slug=slug)
    return render(request, 'blog/news-single.html', {'news': news})