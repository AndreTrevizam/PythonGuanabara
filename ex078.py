numeros = []

for i in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)

maior_valor = max(numeros)
maior_index = numeros.index(maior_valor)

menor_valor = min(numeros)
menor_index = numeros.index(menor_valor)

print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {max(numeros)} na posição {maior_index} ')
print(f'O menor valor digitado foi {min(numeros)} na posição {menor_index} ')