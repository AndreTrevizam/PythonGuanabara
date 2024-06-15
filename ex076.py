tupla = ('Bolacha', 5.99, 'Açucar', 10, 'Arroz', 25.89)

print('=== Tabela de produtos ===')

for pos in range(len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end= ' ')
    else:
        print(f'R$ {tupla[pos]:>7.2f}')