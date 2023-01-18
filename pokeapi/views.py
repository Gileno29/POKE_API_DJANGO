
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

    #nomes={'nomes':nomes}
    figures={'figures': get_figures()}
    context_return=zip(nomes, get_figures())
    context={
        'pokemons': context_return
    }
    return render(request, "index.html",context)




#GET IMAGENS POKEMONS
def get_figures():
    webservice="https://pokeapi.co/api/v2/pokemon"
    req=requests.get(webservice)
    figures=[]

    try:
        pokemons = json.loads(req.content)

    except:
        print("A resposta não chegou com o formato esperado.")
    
    for pokemon in pokemons['results']: 
        pokemon_data=pokemon['url']
        req=requests.get(pokemon_data)

        try:
            pokemons  = json.loads(req.content)
            if pokemons['forms']:
                req_figure=requests.get(pokemons['forms'][0]['url'])
                
                figure=json.loads(req_figure.content)
                #print(figure['sprites']['back_default'])
                figures.append(figure['sprites']['back_default'])

            return figures
        except ValueError:
            print("A resposta não chegou com o formato esperado.")

   
    
        

