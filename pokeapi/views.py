from django.shortcuts import render
import requests



def  index(request):
    webservice="https://pokeapi.co/api/v2/pokemon"
    req=requests.get(webservice)
    try:
        lista = req.json()
    except ValueError:
            print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

        cnt = {
            "municipios": dicionario
        }

    return render(request, "index.html", cnt)


