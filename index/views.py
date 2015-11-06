from django.shortcuts import render
from photos.models import Photo
from users.models import Account
# Create your views here.
def index(request):
    title = 'NTHUFC'
    #test related_name
    '''
    test_account = Account.objects.all()[:1].get()
    all_photos = test_account.photos.all()
    '''
    return render(request, "index/index.html", {"title":title})

def participate(request):
    title = 'Participate'
    return render(request, "index/participate.html", {"title":title})
