from django.urls import path
from app2.views import *
app_name='macha'

urlpatterns=[
    path('nani/',nani,name='nani')
]