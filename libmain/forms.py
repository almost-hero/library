from django import forms
from django.contrib.auth.models import User

class AddUser(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','type':'text','placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','type':'password','placeholder':'Password'
    }))

    class Meta:
        model = User
        fields = ['username','password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username = username)
        if username_qs.exists():
            raise forms.ValidationError('This username is already exist')
        return username
