from django.shortcuts import render
from .models import Article
from django.http import Http404

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

# Create your views here.
