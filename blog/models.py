from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Define your choices
CATEGORY_CHOICES = [
    ('Art & Craft', 'Art & Craft'),
    ('Business', 'Business'),
    ('Technology', 'Tech'),
]


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    body = RichTextField(blank=False, null=False)
    img_url = models.CharField(max_length=200)
    category = models.CharField(max_length=255, default='', choices=CATEGORY_CHOICES)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    # Tells django how to find the url of specific post
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


# Creating the comments table
class Comment(models.Model):
    # Create Foreign Key, "users.id". users refer to the table name of User
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(BlogPost, related_name='comment_s', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)


# Creating the featured post
class FeaturedPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    body = RichTextField(blank=False, null=False)
    img_url = models.CharField(max_length=200)

    # Tells django how to find the url of specific post
    def get_absolute_url(self):
        return reverse('featured_post_detail', kwargs={'pk': self.pk})
