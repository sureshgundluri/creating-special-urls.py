from django.urls import path
from app.views import *
app_name='anitha'
urlpatterns=[
    path('java/',java,name='java'),
]