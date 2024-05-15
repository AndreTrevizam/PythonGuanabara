lado1 = int(input('Digite o valor do lado: '))
lado2 = int(input('Digite o valor do lado: '))
lado3 = int(input('Digite o valor do lado: '))

if lado1 == lado2 and lado2 == lado3:
    print(f'Isso é um triangulo Equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print(f'Isso é um triangulo Isósceles')
elif lado1 != lado2 and lado3 != lado1 and lado2 != lado3:
    print(f'Isso é um triangulo Escaleno')
