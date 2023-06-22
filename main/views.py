from django.shortcuts import render
from django.views.generic import ListView

from .models import BlogPost


class MainPageView(ListView):
    queryset = BlogPost.objects.all()
    context_object_name = 'posts'
    template_name = 'base.html'
