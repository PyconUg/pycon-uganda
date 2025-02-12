"""
Forms and validation code for user registration.

Note that all of these forms assume Django's bundle default ``User``
model; since it's not possible for a form to anticipate in advance the
needs of custom user models, you will need to write your own forms if
you're using a custom model.

"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm

from django.contrib.auth.models import User
from registration.users import UserModel
from registration.users import UsernameField
from registration.utils import _
from django.utils.translation import gettext_lazy as _

# Third Parties
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django_recaptcha.fields import ReCaptchaField


User = UserModel()


from .models import Fin_aid

 


class Fin_aidForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Fin_aid
        fields = ('title', 'financial_assistance', 'user',) 

    def __init__(self, *args, **kwargs):
        super(Fin_aidForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_Fin_aidForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('update', 'Fin_aid '))

