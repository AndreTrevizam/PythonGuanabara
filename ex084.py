pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    opcao = str(input('Quer continuar? [S/N] '))
    if opcao.lower() == 'n':
        break


print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
maior_peso = []
for p in pessoas:
    if p[1] == maior:
        maior_peso.append(p[0])
print(f'O maior peso foi de {maior}Kg. Peso de {maior_peso}')
menor_peso = []
for p in pessoas:
    if p[1] == menor:
        menor_peso.append(p[0])
print(f'O maior menor foi de {menor}Kg. Peso de {menor_peso}')