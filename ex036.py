valor_casa = float(input('Digite o valor da casa: '))
salario = float (input('Digite o seu salário: '))
anos = int(input('Em quantos anos: '))

prestacao = valor_casa / (anos * 12)

if prestacao > salario * 0.3:
    print('Emprestimo negado!')
else:
    print(f'Emprestimo aprovado!')