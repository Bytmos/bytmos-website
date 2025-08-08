from django.contrib import admin
from .models import BlogPost, Comment, FeaturedPost

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(FeaturedPost)
