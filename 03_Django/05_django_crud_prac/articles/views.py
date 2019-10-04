from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content = content)
        article.full_clean()
    except ValidationError:
        raise ValidationError('Your Error message')
    else:
        article.save()
        return redirect('articles:detail', article.pk)