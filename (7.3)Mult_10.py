num = input('Me diga um numero e eu direi se ele é multiplo de 10: ')

num = int(num)

if num % 10 == 0:
    print(f"O numero {num} é multiplo de 10!")
else:
    print(f"O numero {num} não é multiplo de 10!")