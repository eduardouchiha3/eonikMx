from django.urls import path
from eonik.views import *

app_name = 'eonik'

urlpatterns = [
    path('', index, name='index'),
]