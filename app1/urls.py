from django.urls import path
from app1.views import *
app_name='suresh'
urlpatterns=[
    path('python/',python,name='python'),
]