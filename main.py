data = {
    'tomate': 3,
    'limao': 5,
    'cacau': 7,
    'dijei' : {
        'caçamba': 3,
        'tchuchuco' : 5,
        'pirireu' : [0, 1, 2, 3]
    }
}


def adentrar_na_lista(data):
    if type(data) == dict:
        for key in data.keys():
            print(f"{key} - {data[key]}")
            adentrar_na_lista(data[key])
    elif type(data) == list:
        for valor in range(len(data)):
            print(f"{data} - {valor} - {data[valor]}")
            adentrar_na_lista(data[valor])

def forcar_mensagem(tipo, mensagem):
    try:
        resposta = tipo(input(mensagem))
    except:
        print(f"A resposta precisa estar em {tipo}")
        forcar_mensagem(tipo,mensagem)
    finally:
        return resposta
    


lista = [0,1,2,3,4,'a',3]

def forcar_erro(lista):
    for i in range(len(lista)):
        if type(lista[i]) == int:
            print(lista[i])
        else:
            raise TypeError(f"O valor {lista[i]} no indice {i}, não respeita a ordem")

forcar_erro(lista)




