from typing import Dict
from django.urls import path
from .views import indexView, sobreView

urlpatterns = [
    # path(endereço, view.as_view(), name = 'nome-endereço'),
    path('index/', indexView.as_view(), name= 'index'),
    path('', indexView.as_view(), name= 'index'),
    path('about/', sobreView.as_view(), name= 'about'),
]