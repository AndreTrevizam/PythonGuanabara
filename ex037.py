num = int(input('Digite um número inteiro: '))
print('=== Conversão de base ===')
print('1. Binário')
print('2. Octal')
print('3. Hexadecimal')
opcao = int(input('Escolha sua opção: '))

if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])