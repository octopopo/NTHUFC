from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from users.forms import LoginForm
from django.core.urlresolvers import reverse
from photos.models import Photo
# Create your views here.

@login_required
def users(request):
    account = request.user
    photos = account.photos.all()
    return render(request, "users/profile.html", {"photos": photos})

def login(request):
    F = LoginForm
    if request.method == 'GET':
        form = F()
    else:
        form = F(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'])
            if user:
                auth_login(request,user)
                return redirect(reverse('users:profile'))
    ctx = {'form': form}
    return render(request, 'index/login.html', ctx)

def logout(request):
    auth_logout(request)
    return redirect(reverse('index:index'))

@login_required()
def delete_photo(request, delete_id):
    if delete_id != '':
        try:
            Photo.objects.filter(id=long(delete_id)).delete()
            print('Photo id %ld deletes successfully!' % long(delete_id))
        except Photo.DoesNotExist:
            print('Photo id %ld does not exist!' % long(delete_id))

    return redirect(reverse('users:profile'))
