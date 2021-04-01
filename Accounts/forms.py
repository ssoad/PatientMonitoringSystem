from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.forms import ModelForm
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                Tuser = User.objects.filter(username=username)
                if not Tuser:
                    raise forms.ValidationError('This user does not exist')
                if not Tuser[0].check_password(password):
                    raise forms.ValidationError('Incorrect password')
                if not Tuser[0].is_active:
                    raise forms.ValidationError('This user is not active. Please your verification process')
        return super(UserLoginForm, self).clean()
