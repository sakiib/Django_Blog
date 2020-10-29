from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'sakib',
        'title': 'blog post 1',
        'content': 'first post content'
    },
    {
        'author': 'alamin',
        'title': 'blog post 2',
        'content': 'second post content'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
