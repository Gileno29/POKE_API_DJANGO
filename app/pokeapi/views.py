from django.shortcuts import render
import requests
import json

#DEFAULT WEB SERVICE FOR CONSULT
WEB_SERVICE="https://pokeapi.co/api/v2/pokemon/"


def  index(request):
    req=requests.get(WEB_SERVICE)
    try:
        pokemons  = json.loads(req.content)

    except ValueError:
        print("A resposta não chegou com o formato esperado.")
   
    nomes= []
    
    for pokemon in pokemons['results']:
        nomes.append(pokemon['name']) 
 


    try:
        context_return=zip(nomes, get_figures())
        context={
            'pokemons': context_return
        }
    except Exception as e:
        pass

    return render(request, "index.html",context)




#GET IMAGENS POKEMONS
def get_figures():
    req=requests.get(WEB_SERVICE)
    figures=[]
    pokemon_data=[]
    pokemon_url_figure=[]
    try:
        pokemons = json.loads(req.content)

    except:
        print("A resposta não chegou com o formato esperado.")
    
    for p in range (len(pokemons['results'])): 
        print('Esses são os results: ', type(pokemons['results']), len(pokemons['results']))
        print('Pokemons: ', pokemons['results'][p]['url'])
        pokemon_data.append(pokemons['results'][p]['url'])

    for p in pokemon_data:     
        req=requests.get(p)
        try:
            pokemons  = json.loads(req.content)
            #print(type(pokemons))
            
            #print(pokemons['forms'])
            pokemon_url_figure.append(pokemons['forms'])

                        
        except Exception as e:
            continue
            

    remover=":'}]"

    for i in pokemon_url_figure:
        #print(i, type(i), len(i))
        url= str(i).split('url')[1].replace(remover,'').strip()
        #print(url)
        req_figure=requests.get(url.replace("'}]", "").replace("': '", ""))
        
        figure=json.loads(req_figure.content)

        #print(figure['sprites']['front_default'])
        figures.append(figure['sprites']['front_default'])
    return figures

    
def format_string(caracteres, t):
    palavra=''
    for i in caracteres:
        if palavra=='':
            palavra=t.replace(i)
        else:
            palavra=palavra
        
    


        

