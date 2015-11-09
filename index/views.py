from django.shortcuts import render, redirect
from photos.models import Photo
from users.models import Account, Author, Book
from index.forms import AccountCreationFrom, AuthorForm, BookForm
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

def participate(request, id_author=None):
    title = 'Participate'
    if id_author is None:
        author = Author()
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=3, can_delete=False)
    else:
        author = Author.objects.get(pk=id_author)
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=3, can_delete=True)


    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author, prefix="main")
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author, prefix="nested")

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse('index:index'))
    else:
        form = AuthorForm(instance=author, prefix="main")
        formset = BookInlineFormSet(instance=author, prefix="nested")

    #return render(request, "test_app/manage_books.html", {"form":form, "formset": formset})
    return render(request, "index/participate.html", {"title": title,"form":form, "formset": formset})
