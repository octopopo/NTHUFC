# -*- coding: utf-8 -*-
from django import forms
from users.models import Account, Author, Book
from photos.models import Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Field, Div
from crispy_forms.bootstrap import  FormActions, InlineRadios

class AccountCreationFrom(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'major', 'year_in_school', 'remarks')

    def __init__(self, *args, **kwargs):
        super(AccountCreationFrom, self).__init__(*args, **kwargs)
        # Set layout for fields.
        self.helper = FormHelper()

        self.fields['remarks'].widget.attrs['rows'] = 4
        self.fields['remarks'].widget.attrs['columns'] = 15

        self.fields['username'].label = u'姓名'
        self.fields['major'].label = u'系所'
        self.fields['year_in_school'].label = u'年級'
        self.fields['remarks'].label = u'備註'

        self.helper.layout = Layout(
            Fieldset(
                u'報名資料',
                Field('username'),
                Field('major'),
                InlineRadios('year_in_school'),
                Field('remarks'),
                HTML('<br>')
            ),
            #type="Submit" name="submit" value="確定送出" class="btn btn-primary"
            #FormActions(
                #Submit('submit', u'確定送出', css_class='btn btn-primary'),
                #css_class="submit-btn"
            #)
        )

class PhotoCreationForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'content', 'tags', 'image')

    def __init__(self, *args, **kwargs):
        super(PhotoCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['content'].widget.attrs['rows'] = 4
        self.fields['content'].widget.attrs['columns'] = 15

        self.helper.layout = Layout(
            Fieldset(
                u'上傳相片',
                Field('title'),
                Field('content'),
                Field('tags'),
                Field('image'),
                HTML('<br>')
            ),
        )

class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
        )
        super(AuthorForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Author

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
        )
        super(BookForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Book
