from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'NTHUFC'
    return render(request, "index/index.html", {"title":title})

def participate(request):
    title = 'Participate'
    return render(request, "index/participate.html", {"title":title})
