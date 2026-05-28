from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from users.models import User
from users.validators import validate_github


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = self.fields.pop('username')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'avatar', 'phone', 'github_url', 'about']
        widgets = {'about': forms.Textarea(attrs={'rows': 4})}

    def clean_github_url(self):
        value = self.cleaned_data.get('github_url')
        if value:
            validate_github(value)
        return value


class UserPasswordChangeForm(PasswordChangeForm):
    pass
