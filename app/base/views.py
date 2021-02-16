from django.shortcuts import render

def top(request):
    ctx = {'title': 'Django学習ちゃんねる'}
    return render(request, 'base/top.html', ctx)

# Create your views here.
