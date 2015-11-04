from django.shortcuts import render

# Create your views here.
def photos(request):
    return render(request, "photos/photos.html", {})
