lista = []

while True:
    num = int(input('Digite um valor: '))
    print('Valor adicionado com sucesso...')
    opcao = input('Quer continuar: (s/n)')

    if num in lista:
        continue
    lista.append(num)

    if opcao.lower() == 'n':
        break


print(sorted(lista))