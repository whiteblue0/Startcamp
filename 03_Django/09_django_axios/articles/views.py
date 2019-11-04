from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Article,Comment, Hashtag
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse,HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
import hashlib
from IPython import embed
# Create your views here.

def index(request):
    # 1. sessions 정보에서 visits_num 이라는 키로 접근해 값을 가져온다
    # 해당하는 키가 없으면 0을 가져옴
    # embed()
    visits_num = request.session.get('visits_num',0)

    # 2. 가져온 값을 sessions에 'visits_nmum'이라는 새로운 키의 값으로 1식 증가
    request.session['visits_num'] = visits_num + 1

    # 3. sessions data를 수정하면 Django는 수정한 내용을 알 수 없어서 작성하는 구문
    request.session.modified = True
    
    articles = Article.objects.all()
    context = {'articles':articles,'visits_num': visits_num, }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    """
    Form Class
    모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 
    데이터 정제 후 DB에 저장하는 로직 필요

    Model Form
    Model에 대한 정보(schema)를 알고 있기 때문에 어떤 모델에 레코드르 넣어야 하는지
    알고 있음. form.save()만 해도 DB에 저장됨
    """
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            # form.cleaned_data를 통해 폼 데이터를 정제한다.(type(form.cleaned_data) = dict)
            article = form.save(commit=False)
            article.user_id = request.user.id
            article.save()
            # 1. content를 공백 기준으로 리스트로 변경 후 for문
            for word in article.content.split():
                # 2. '#' 시작하는 요소를 선택
                if word.startswith('#'):
                    # 3. word와 같은 해시태그를 확인, 기존 객체가 없으면 새로운 객체 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # 4. 게시글의 해시태그 목록에 해당 단어 추가
                    article.hashtags.add(hashtag)
            return redirect('articles:detail', article.pk )
    else:
        form = ArticleForm()
        # embed()
    context = {'form':form, }
    return render(request, 'articles/form.html', context)

def detail(request,article_pk):
    get_object_or_404(Article,pk=article_pk)
    article = Article.objects.get(pk=article_pk)
    commentform = CommentForm()
    comments = article.comments.all()
    person = get_object_or_404(get_user_model(), pk=article.user.pk)
    context = {'article':article, 
    'commentform': commentform, 
    'comments': comments,
    'person': person
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request,article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if request.user == article.user:
            article.delete()
    return redirect('articles:index')


@login_required
def update(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST' :
            # instance -> 수정의 대상이 되는 특정한 글 객체
            form = ArticleForm(request.POST,instance=article)
            if form.is_valid():
                form.save()
                article.hashtags.clear()
                for word in article.content.split():
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article.pk)

    context = {'form':form,'article':article,}
    return render(request, 'articles/form.html', context)

"""
Create 로직
1.GET
 - 사용자가 데이터를 입력할 수 있는 Form을 제공
2. POST
 - 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1.GET
 - 기존 사용자의 글이 입력된 Form 제공
2.POST
 - 수정된 글을 DB에 저장
"""

@require_POST
def comments_create(request,article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.article_id = article_pk
            comment.user_id = request.user.id
            comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request,article_pk,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@login_required
def like(request, article_pk):
    if request.is_ajax():
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            liked= False
        else:
            article.like_users.add(user)
            liked= True
        context = { 
            'liked': liked,
        'count': article.like_users.count(),
        }
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()


@login_required
def follow(request, article_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user

    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('articles:detail', article_pk)

@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {'hashtag':hashtag, 'articles':articles, }
    return render(request, 'articles/hashtag.html', context)
    