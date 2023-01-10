from django.urls import path
from app1.views import *
app_name='mawa'

urlpatterns=[
    path('anand/',anand,name='anand')
]