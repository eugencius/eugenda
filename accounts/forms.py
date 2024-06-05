from django import forms
from django.contrib.auth import get_user_model

from templates.utils import set_placeholder

User = get_user_model()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        set_placeholder(self.fields['username'], 'Your username')
        set_placeholder(self.fields['password'], 'Password')
        set_placeholder(
            self.fields['confirm_password'], 'Confirm your password')
        set_placeholder(self.fields['first_name'], 'Your first name')
        set_placeholder(self.fields['last_name'], 'Your last name')

        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {'class': 'field-input'})

    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", 'password',
                  'confirm_password', 'first_name', 'last_name']

        widgets = {
            "password": forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if first_name == last_name:
            raise forms.ValidationError({
                'first_name': 'First and last name cannot be equal',
                'last_name': 'First and last name cannot be equal',
            })

        if password != confirm_password:
            raise forms.ValidationError({
                'password': 'The both password fields must be equal',
                'confirm_password': 'The both password fields must be equal',
            })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()

        if exists:
            raise forms.ValidationError(
                "This username is already being used", code='invalid'
            )

        return username
