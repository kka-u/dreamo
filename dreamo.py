import random as r
from colorama import Fore, Style, init

palavras = {
    '1': 'amora',
    '2': 'araça',
    '3': 'aveia',
    '4': 'avelã',
    '5': 'arroz',
    '6': 'aipim',
    '7': 'apelo',
    '8': 'apego', 
    '9': 'alado',
    '10': 'ajuda'
}

palavra = r.choice(list(palavras.values()))

tentativa = input('digite sua tentativa --> ')

def comparar(palavra, tentativa):
    resultado = ['cinza'] * len(tentativa)
    letras_disponiveis = list(palavra)

    for i in range(len(tentativa)):
        if tentativa[i] == palavra[i]:
            resultado[i] == 'verde'
            letras_disponiveis[i] = None

    for i in range(len(tentativa)):
        if resultado[i] == 'verde':
            continue
        if tentativa[i] in letras_disponiveis:
            resultado[i] == 'amarelo'
            letras_disponiveis[letras_disponiveis.index(tentativa[i])] = None

    print(resultado)        

    return resultado

comparar(palavra, tentativa)