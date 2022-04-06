
from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('pokemons', views.index, name='pokemons'),
    #path('teste_filtros', views.testefiltro, name='teste_filtros')
]