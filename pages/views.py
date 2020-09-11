from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def comments(request):
    return render(request, 'comments.html')