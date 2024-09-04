sandwich_orders = ['presunto','misto','salsicha','hamburguer']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f'Seu sanduiche de {sandwich} está pronto!')
    finished_sandwiches.append(sandwich)


print(f"Esses são todos os sanduiches feitos hoje:\n{finished_sandwiches}")