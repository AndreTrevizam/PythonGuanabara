menor = 0
maior = 0
for c in range(1,6):
    peso = float(input(f'Peso da {c} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Menor peso = {menor}')
print(f'Maior peso = {maior}')