from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost, FeaturedPost


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["home", "about", "faqs", "contact", "bytmos-partner"]

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj: object) -> object:
        return obj.date_posted


class FeaturedPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return FeaturedPost.objects.all()

    def lastmod(self, obj):
        return obj.date_posted
