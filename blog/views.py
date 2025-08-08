from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from .models import BlogPost, FeaturedPost
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def blog_home(request):
    context = {
        "posts": BlogPost.objects.all(),
        "featured_post": BlogPost.objects.all().first(),
    }


class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        # Get the original queryset
        queryset = super().get_queryset()
        # Skip the first item using slicing
        return queryset[4:]

    def get_context_data(self,  **kwargs):
        # Call the base implementation to get the existing context
        context = super().get_context_data(**kwargs)

        # Add additional context variables
        context["most_recent_post"] = BlogPost.objects.all().last()
        context["recent_posts"] = BlogPost.objects.all().order_by('-date_posted')[1:4]
        context["featured_post"] = FeaturedPost.objects.all().last()
        context['year'] = datetime.now().year  # Pass just the year
        return context


class BusinessCategoryListView(ListView):
    model = BlogPost
    template_name = 'blog/business_category.html'
    context_object_name = 'business_posts'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        """Return the filtered queryset for the view."""
        return BlogPost.objects.filter(category="Business")

    def get_context_data(self, **kwargs):
        """Add additional context variables to the context."""
        context = super().get_context_data(**kwargs)

        # Fetch the filtered queryset
        business_posts = self.get_queryset()

        # Add additional context variables
        context["most_recent_post"] = business_posts.last()
        context["recent_posts"] = business_posts.order_by('-date_posted')[1:4]
        context["featured_post"] = FeaturedPost.objects.all().last()

        return context


class TechCategoryListView(ListView):
    model = BlogPost
    template_name = 'blog/tech_category.html'
    context_object_name = 'tech_posts'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        """Return the filtered queryset for the view."""
        return BlogPost.objects.filter(category="Tech")

    def get_context_data(self, **kwargs):
        """Add additional context variables to the context."""
        context = super().get_context_data(**kwargs)

        # Fetch the filtered queryset
        business_posts = self.get_queryset()

        # Add additional context variables
        context["most_recent_post"] = business_posts.last()
        context["recent_posts"] = business_posts.order_by('-date_posted')[1:4]
        context["featured_post"] = FeaturedPost.objects.all().last()

        return context


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

    def get_context_data(self,  **kwargs):
        # Call the base implementation to get the existing context
        context = super().get_context_data(**kwargs)

        # Add additional context variables
        context["most_recent_post"] = BlogPost.objects.all().last()
        context["recent_posts"] = BlogPost.objects.all().order_by('-date_posted')[1:4]
        context["posts"] = BlogPost.objects.all()
        context["featured_post"] = FeaturedPost.objects.all().last()

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'subtitle', 'img_url', 'category', 'body',]

    # Making the current user the author of the post before the form is submitted
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden('You must be logged in to create a blog post')

        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'subtitle', 'body', 'category', 'img_url']

    # Making the current user the author of the post before the form is submitted
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden('You must be logged in to create a blog post')

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# Creating featured post models
class FeaturedPostCreateView(LoginRequiredMixin, CreateView):
    model = FeaturedPost
    template_name = 'blog/featured_post_form.html'
    fields = ['title', 'img_url', 'body']

    # Making the current user the author of the post before the form is submitted
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden('You must be logged in to create a blog post')

        form.instance.author = self.request.user
        return super().form_valid(form)


class FeaturedPostListView(ListView):
    model = FeaturedPost
    template_name = 'blog/index.html'
    context_object_name = 'featured_post'


class FeaturedPostDetailView(DetailView):
    model = FeaturedPost
    template_name = 'blog/featured_post_detail.html'

    def get_context_data(self,  **kwargs):
        # Call the base implementation to get the existing context
        context = super().get_context_data(**kwargs)

        # Add additional context variables
        context["posts"] = BlogPost.objects.all()
        context["recent_posts"] = BlogPost.objects.all().order_by('-date_posted')[1:4]

        return context
