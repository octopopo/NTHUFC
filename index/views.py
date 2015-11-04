from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index/index.html", {})

def sign_up(request):
    return render(request, "index/sign_up.html", {})
