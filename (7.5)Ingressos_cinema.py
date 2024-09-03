print('Bem vindo ao cinema!')

while True:
    age = input('Por favor, digite sua idade: ')
    age = int(age)
    if age < 3:
        print('O ingresso é gratuito')
    elif age > 3 and age <= 12:
        print('O ingresso custa R$10')
    else:
        print('O ingresso custa R$15')



