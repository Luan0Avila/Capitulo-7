response = {}
flag = True

while flag:
    nome = input('Qual seu nome? ')
    lugar = input(f'Olá {nome}, se você pudesse visitar qualquer lugar do mundo, para onde iria? ')

    response[nome] = lugar

    repete = input('Gostaria de repetir mais uma vez?(s/n) ')
    if repete == 'n':
        flag = False

for nome, lugar in response.items():
    print(f"{nome.title()} gostaria de visitar {lugar.title()}")
