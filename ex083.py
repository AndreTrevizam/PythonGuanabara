expressao = input('Escreva uma expressão: ')

lista = []

for parenteses in expressao:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão foi válidada!')
else:
    print('Sua expressão não foi válidada!')