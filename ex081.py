lista = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opcao = input('Deseja continuar? (S/N): ')
    if opcao.lower() == 'n':
        break

print(f'Valores digitados {lista}')

print(f'Foram digitados {len(lista)} números')

print(f'Valores em ordem decrescente: {sorted(lista, reverse=True)}')

if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista')
else:
    print(f'O valor 5 não foi digitado e não está na lista')