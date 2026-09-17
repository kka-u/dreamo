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





def comparar(palavra, tentativa):
    resultado = ['cinza'] * len(tentativa)
    letras_disponiveis = list(palavra)

    for i in range(len(tentativa)):
        if tentativa[i] == palavra[i]:
            resultado[i] = 'verde'
            letras_disponiveis[i] = None

    for i in range(len(tentativa)):
        if resultado[i] == 'verde':
            continue
        if tentativa[i] in letras_disponiveis:
            resultado[i] = 'amarelo'
            letras_disponiveis[letras_disponiveis.index(tentativa[i])] = None

    return resultado


init()
def mostrar_resultado(tentativa, resultado):
    cores = {
        'cinza': Fore.WHITE,
        'verde': Fore.GREEN,
        'amarelo': Fore.YELLOW
    }

    saida = ''

    for letra, cor in zip(tentativa, resultado):
        saida += cores[cor] + letra + Style.RESET_ALL

    return saida

def jogar(palavra):
    tentativa = input('digite sua tentativa(apenas 5 letras) --> ')
    tentativas = 0

    while tentativas < 6:

        if len(tentativa) != len(palavra):
            tentativa = input(f'tentativa precisa ter {len(palavra)} letras! tente de novo --> ')
            continue

        if tentativa != palavra:
            resultado = comparar(palavra, tentativa)
            tentativas += 1
            print(mostrar_resultado(tentativa, resultado))
            tentativa = input('tente novamente(apenas 5 letras) --> ')
        else:
            tentativas += 1
            resultado = comparar(palavra, tentativa)
            plural = 'tentativa' if tentativas == 1 else 'tentativas'
            print(f'Parabéns! você acertou em {tentativas} {plural}!')
            return mostrar_resultado(tentativa, resultado)

jogar(palavra)

