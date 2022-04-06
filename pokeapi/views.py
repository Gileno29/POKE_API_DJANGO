from traceback import print_tb
from django.shortcuts import render
import requests
import json


def convert(lst):
    for l in lst:
        print(l)
 
        dados={
            'nome': l['nome'],
            'url': l['url']
        }

    return dados

def  index(request):
    webservice="https://pokeapi.co/api/v2/pokemon"
    req=requests.get(webservice)
    try:
        pokemons  = json.loads(req.content)

    except ValueError:
            print("A resposta não chegou com o formato esperado.")

    
    print(pokemons['results'])
    
   


    return render(request, "index.html", convert(pokemons['results']))


