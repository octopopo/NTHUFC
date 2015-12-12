from django.shortcuts import render
from .upload import uploadPhoto
# Create your views here.
def photos(request):
    return render(request, "photos/photos.html", {})

def upload(request,photo_id):
	response = uploadPhoto(photo_id)
	return render(request, "photos/upload.html", {'response':response})
