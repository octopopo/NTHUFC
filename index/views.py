from django.shortcuts import render, redirect
from photos.models import Photo
from users.models import Account
from index.forms import AccountCreationFrom
from django.core.urlresolvers import reverse

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
    if request.method == 'POST':
        form = AccountCreationFrom(request.POST)
        if form.is_valid():
            account = form.save()
            account.backend = 'django.contrib.auth.backends.ModelBackend'
            return redirect(reverse('index:index'))
    else:
        form = AccountCreationFrom()
    return render(request, "index/participate.html", {"title": title, "form": form})
