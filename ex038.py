num = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite um valor inteiro: '))

if num > num2:
    print(f'{num} é maior que {num2}')
elif num2 > num:
    print(f'{num2} é maior que {num}')
elif num == num2:
    print(f'Os números são iguais')
