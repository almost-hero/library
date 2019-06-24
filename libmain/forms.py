from django import forms
from django.contrib.auth.models import User
from .models import Book

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

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','slug','author','date']
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Add book title'}),
                'slug':forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Add book slug'}),
                'author':forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Add book author'}),
                'date':forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Add book date'}),

        }
