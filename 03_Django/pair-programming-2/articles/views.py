from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm,CommentForm

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        articleform = ArticleForm(request.POST)
        article = articleform.save()
        return redirect('articles:detail', article.pk)
    
    articleform = ArticleForm()
    context = {'articleform':articleform, }
    return render(request, 'articles/forms.html',context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    commentform = CommentForm()
    context = {'article': article, 'comments': comments, 'commentform':commentform, }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        articleform = ArticleForm(request.POST, instance=article)
        articleform.save()
        return redirect('articles:detail', article.pk)
    articleform = ArticleForm(instance=article)
    context = {'articleform':articleform, }
    return render(request, 'articles/forms.html', context)


def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        comment = commentform.save(commit=False)
        comment.article_id = article.pk
        comment.save()
        return redirect('articles:detail', article.pk)
    commentform = CommentForm()
    context = {'commentfrom': commentform, }
    return render(request, 'articles/detail.html', context)


def comments_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = article.comments.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article.pk)