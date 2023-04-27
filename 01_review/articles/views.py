from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def greeting(request):
    return render(request, 'hello.html', { 'name': 'Deon' })

def intro(request):
    fruits = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Deon',
        'koreanAge': 30
    }
    context = {
        'fruits': fruits,
        'info': info
    }
    return render(request, 'intro.html', context)