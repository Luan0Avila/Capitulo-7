sandwich_orders = ['pastrami', 'presunto', 'misto', 'pastrami','salsicha','hamburguer','pastrami']
finished_sandwiches = []
print(f'Estes são os nossos pedidos:\n{sandwich_orders}\n')

print('Informamos que no momento a lanchonete está sem pastrami, lamentamos por isso!\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f'Seu sanduiche de {sandwich} está pronto!')
    finished_sandwiches.append(sandwich)


print(f"\nEsses são todos os sanduiches feitos hoje:\n{finished_sandwiches}")
