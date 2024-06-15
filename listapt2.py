# dados = []
# dados.append('Pedro')
# dados.append('25')

# pessoas = []
# pessoas.append(dados[:])

# print(pessoas[0])
# print(pessoas[0][0])

# galera = [['Pedro', 18], ['Julia', 19], ['João', 20]]
# for p in galera:
#     print(p[0])

galera = []
dado = []
for i in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 20:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')