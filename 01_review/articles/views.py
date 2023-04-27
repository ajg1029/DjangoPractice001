from django.shortcuts import render

import random

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

def dinner(request):
    foods = ['햄버거', '감튀', '콜라', '텐더칰힌']
    pick = random.choice(foods)
    context = {
        'foods': foods,
        'pick': pick,
    }
    return render(request, 'dinner.html', context)