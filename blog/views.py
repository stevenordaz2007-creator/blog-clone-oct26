from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'read.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'