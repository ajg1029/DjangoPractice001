from django.shortcuts import render
from .models import Article

def index(request): # 작성한 모든 게시글을 출력
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')

# def detial(request):
#     return render(request, 'articles/detial.html')

# def delete(request):
#     return render(request, 'articles/delete.html')

# def edit(request):
#     return render(request, 'articles/edit.html')

# def update(request):
#     return render(request, 'articles/update.html')
