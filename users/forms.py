# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Field, Div
from crispy_forms.bootstrap import  FormActions, InlineRadios
from users.models import Account

class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # important!!!!! self.helper.form_tag = False
        self.helper.form_tag = False

        self.fields['username'].label = u'姓名'
        self.fields['email'].label = u'信箱'
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    u'登入',
                    Field('username'),
                    Field('email'),
                    HTML('<br>')
                ),
                FormActions(
                    Submit('submit', u'登入', css_class='btn btn-primary'),
                    css_class="submit-btn"
                ),
                css_class="login-form",
            ),
        )


    def clean_email(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")

        try:
            user = Account.objects.get(username=username, email=email)
        except Account.DoesNotExist:
            raise forms.ValidationError("Username or email is wrong.")

        return email
