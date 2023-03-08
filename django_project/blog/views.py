from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Posts'
    }
    return render(request, 'blog/home.html', context)


# List View
class PostListView(ListView):
    model = Post  # el model elly hymello list
    template_name = 'blog/home.html'  # which template to render
    context_object_name = 'posts' # esm el variable elly hyro7 el html
    ordering = ['-date_posted']  # 3ayzny arateb el list based 3ala eh ?


# To show the details of a single instance of the model
class PostDetailView(DetailView):
    model = Post  # el model elly hymello list


# To create new instance of the model
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # el model elly hymello list
    fields = ['title', 'content'] # el fields elly me7tagenha 3shan n3mel create

    def get_success_url(self):
        return reverse("blog-home")

    # We need to till django that the author that will greate the post is the authenticated user
    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # el model elly hymello list
    fields = ['title', 'content'] # el fields elly me7tagenha 3shan n3mel create

    def get_success_url(self):
        return reverse("blog-home")

    # We need to till django that the author that will greate the post is the authenticated user
    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

