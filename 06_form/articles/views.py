from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    # 게시글 정렬 변경
    
    # 1. 응답받은 queryset을 나중에 python으로 정렬
    # articles = Article.objects.all()[::-1]

    # 2. 처음부터 DB에게 원하는 정렬로 쿼리셋을 만들어 주도록 요청을 보냄(DB가 정렬)
    # articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')

#     # article = Article(title=title, content=content)
#     # article.save()
    
#     form = ArticleForm(request.POST)
#     # 유효성 검사
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     return redirect('articles:new')

# # article.save() --> DB에 저장
# # form.save() --> 객체를 만들고 DB에 저장. 객체를 만듦 = 반환값이 있음
# # 그 반환값을 article 에 저장해서 템플릿으로 넘겨줌

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
        




def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
