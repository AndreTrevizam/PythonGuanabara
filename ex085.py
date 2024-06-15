todos_numeros = []
pares = []
impares = []

for i in range(7):
    todos_numeros.append(int(input(f'Digite o {i+1}. valor: ')))

for n in todos_numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores impares digitados foram: {sorted(impares)}')