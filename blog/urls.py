from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    FeaturedPostCreateView,
    FeaturedPostDetailView,
    BusinessCategoryListView,
    TechCategoryListView
)
from . import views


urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog_home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('featured/new/', FeaturedPostCreateView.as_view(), name='featured_post_create'),
    path('featured/<int:pk>/', FeaturedPostDetailView.as_view(), name='featured_post_detail'),
    path('blog/business/', BusinessCategoryListView.as_view(), name='business_category'),
    path('blog/tech/', TechCategoryListView.as_view(), name='tech_category'),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]





