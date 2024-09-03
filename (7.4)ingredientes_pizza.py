while True:
   sair = input('Gostaria de adicionar algum ingrediente?(s/n)')
   if sair == 's':
        ingr = input('Insira um ingrediente a pizza: ')
        print(f"{ingr} está sendo adicionado a pizza.")
   elif sair == 'n':
        print('Obrigado, sua pizza logo estará pronta!')
        break
   else:
       print('Por favor selecione uma opção válida.')
    
    