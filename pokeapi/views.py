
from traceback import print_tb
from unicodedata import name
from django.shortcuts import render
import requests
import json

def convert(lst):
    indice =0 
    dados={}
    for l in lst:   
        dado={
                'nome':l['name'],
                'url': l['url']
            }
        #print(dados)
        dados[indice]=dado
        indice=indice+ 1
    
    return dados



def  index(request):
    webservice="https://pokeapi.co/api/v2/pokemon/"
    req=requests.get(webservice)
    try:
        pokemons  = json.loads(req.content)

    except ValueError:
            print("A resposta não chegou com o formato esperado.")
   
    nomes= []
    
    for pokemon in pokemons['results']:
      
        
        nomes.append(pokemon['name']) 
    print(nomes)

    nomes={'nomes':nomes}
    return render(request, "index.html",nomes)







def imagens(request):
    webservice="https://pokeapi.co/api/v2/pokemon"
    req=requests.get(webservice)

    try:
        pokemons = json.loads(req.content)

    except:
        print("A resposta não chegou com o formato esperado.")

    return render(request,  pokemons)

        

