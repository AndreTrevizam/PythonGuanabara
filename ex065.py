media = 0
count = 0
for c in range(4):
    nome = input(f'Digite o nome da {c+1} pessoa:')
    idade = int(input(f'Digite a idade da {c+1} pessoa:'))
    sexo = input(f'Digite o sexo da {c+1} pessoa(m/h):')

    if sexo == 'm':
        if idade < 20:
            count += 1

media += idade / 4    

print(f'A média de idade do grupo é {media:.1f}')
print(f'O homem mais velho do grupo se chama: ')
print(f'Temos {count} mulheres abaixo dos 20 anos')