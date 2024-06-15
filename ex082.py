lista = []
lista_pares = []
lista_impares = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

    opcao = input('Deseja continuar? (S/N): ')
    if opcao.lower() == 'n':
        break

print(f'Números digitados {lista}')
print(f'Números pares {lista_pares}')
print(f'Números impares {lista_impares}')