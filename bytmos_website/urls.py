from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.urls import path, include
from users import views as user_views
from django.contrib.sitemaps.views import sitemap
from users.views import logout_user
from personal.sitemaps import StaticViewSitemap, BlogPostSitemap, FeaturedPostSitemap
from django.views.generic.base import TemplateView
from personal.views import (
    home, bytmos_partner,
    about, faqs, terms, privacy
)


sitemaps = {
    "static_site_map": StaticViewSitemap,
    "blog_site_map": BlogPostSitemap,
    "featured_post_site_map": FeaturedPostSitemap

}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('faqs/', faqs, name='faqs'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('bytmos_partner/', bytmos_partner, name='bytmos_partner'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path("", include("personal.urls")),
    # path('profile/', profile_views.profile, name='profile'),
    path('', include('blog.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]


