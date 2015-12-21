#-*- encoding=UTF-8 -*-
from django.shortcuts import render, redirect
from photos.models import Photo
from users.models import Account
from index.forms import AccountCreationFrom, PhotoCreationForm
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory


from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from index.forms import LoginForm

from photos.socialApplication import uploadPhoto

# Create your views here.
def index(request):
    #test related_name
    '''
    test_account = Account.objects.all()[:1].get()
    all_photos = test_account.photos.all()
    '''
    return render(request, "index/index.html", {})

def participate(request, id_account=None):
    if id_account is None:
        account = Account()
        PhotoInlineFormSet = inlineformset_factory(Account, Photo,
            form=PhotoCreationForm, max_num=5, validate_max=True,
            min_num=1, validate_min=True, extra=5, can_delete=False)
    else:
        account = Account.objects.get(pk=id_account)
        PhotoInlineFormSet = inlineformset_factory(Account, Photo,
            form=PhotoCreationForm, max_num=5, validate_max=True,
            min_num=1, validate_min=True, extra=5, can_delete=True)


    if request.method == "POST":
        form = AccountCreationFrom(request.POST, request.FILES, instance=account, prefix="main")
        formset = PhotoInlineFormSet(request.POST, request.FILES, instance=account, prefix="nested")

        if form.is_valid() and formset.is_valid():
            form.save()
            photoList = formset.save(commit=False)
            for photo in photoList:
                print photo.title
                photo.save()
                response = uploadPhoto(photo)
            return redirect(reverse('index:index'))
    else:

        form = AccountCreationFrom(instance=account, prefix="main")
        formset = PhotoInlineFormSet(instance=account, prefix="nested")


    return render(request, "index/participate.html", {"form":form, "formset": formset})

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
