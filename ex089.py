lista_composta = []

while True:
    nome = input('Nome: ')
    notas = []
    for i in range(2):
        nota = float(input(f'Nota {i+1}: '))
        notas.append(nota)
    
    lista_composta.append([nome, notas])
   
    opcao = input('Quer continuar? [S/N]')
    if opcao.lower() == 'n':
        break

print(f'-='*20)
print('No. Nome           MÉDIA')
print('-----------------------------')
for index, aluno in enumerate(lista_composta):
    nome = aluno[0]
    notas = aluno[1]
    media = sum(notas) / len(notas)
    print(f'{index:<4}{nome:<10}{media:>8.1f}')
print('-----------------------------')

while True:
    mostrar_nota = input('Mostrar notas de qual aluno? (fim interrompe): ')
    if mostrar_nota.lower() == 'fim':
        break
    if mostrar_nota == nome:
        print(f'Notas de {nome} são {notas}')
    


    
