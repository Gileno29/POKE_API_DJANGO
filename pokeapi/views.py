from django.shortcuts import render
import requests
import json

#DEFAULT WEB SERVICE FOR CONSULT
WEB_SERVICE="https://pokeapi.co/api/v2/pokemon/"

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
    req=requests.get(WEB_SERVICE)
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
    req=requests.get(WEB_SERVICE)
    figures=[]
    pokemon_data=[]
    try:
        pokemons = json.loads(req.content)

    except:
        print("A resposta não chegou com o formato esperado.")
    
    for pokemon in pokemons['results']: 
        pokemon_data.append(pokemon['url'])
        for p in pokemon_data:
            req=requests.get(p)
            try:
                pokemons  = json.loads(req.content)
                #print(pokemons)
               
                for i in pokemons:
                    print()
                    if i=='forms':
                        for p in pokemons[i]: 
                            req_figure=requests.get(p['url'])
                            
                            figure=json.loads(req_figure.content)

                            print(figure)
                            figures.append(figure['sprites']['front_default'])


        
            except ValueError:
                print("A resposta não chegou com o formato esperado.")
            
        print(figures)
        return figures

   
    
        

