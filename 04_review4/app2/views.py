from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'app2/hello.html')