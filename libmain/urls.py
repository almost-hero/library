from django.urls import path
from .views import *

urlpatterns = [
    path('', users_list, name='users_list_url'),
    path('user/<id>/',user_detail,name='user_detail_url')
]
