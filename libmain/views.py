from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import *

# Create your views here.
def users_list(request):
    users = User.objects.all()
    form = AddUser(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password= password)
    return render(request,'libmain/users_list.html',{'users':users,'form':form})
