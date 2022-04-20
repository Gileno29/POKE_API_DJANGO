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
    webservice="https://pokeapi.co/api/v2/pokemon"
    req=requests.get(webservice)
    try:
        pokemons  = json.loads(req.content)

    except ValueError:
            print("A resposta não chegou com o formato esperado.")

    print(pokemons['results'][0]['name'])
    
    pokemons={
        'pokemons':convert(pokemons['results'])
    }

    return render(request, "index.html",pokemons)


