from django.shortcuts import render, redirect
from photos.models import Photo
from users.models import Account, Author, Book
from index.forms import AccountCreationFrom, AuthorForm, BookForm, PhotoCreationForm
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory

# Create your views here.
def index(request):
    title = 'NTHUFC'
    #test related_name
    '''
    test_account = Account.objects.all()[:1].get()
    all_photos = test_account.photos.all()
    '''
    return render(request, "index/index.html", {"title":title})

def participate(request, id_account=None):
    title = 'Participate'
    if id_account is None:
        account = Account()
        PhotoInlineFormSet = inlineformset_factory(Account, Photo, form=PhotoCreationForm, extra=3, can_delete=False)
    else:
        account = Account.objects.get(pk=id_account)
        PhotoInlineFormSet = inlineformset_factory(Account, Photo, form=PhotoCreationForm, extra=3, can_delete=True)


    if request.method == "POST":
        form = AccountCreationFrom(request.POST, request.FILES, instance=account, prefix="main")
        formset = PhotonlineFormSet(request.POST, request.FILES, instance=account, prefix="nested")

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse('index:index'))
    else:
        form = AccountCreationFrom(instance=account, prefix="main")
        formset = PhotoInlineFormSet(instance=account, prefix="nested")

    #return render(request, "test_app/manage_books.html", {"form":form, "formset": formset})
    return render(request, "index/participate.html", {"title": title,"form":form, "formset": formset})
