numeros = []

for i in range(4):
    num = int(input('Digite um número: '))

    numeros.append(num)

tupla = tuple(numeros)

print(f'Você digitou os números {tupla}')

print('-=' * 15)

count = 0
for c in tupla:
    if c == 9:
        count += 1


print(f'O número nove aparece {count} vezes!')
print('-=' * 15)

#em que posiçao foi digitado o primeiro valor 3
print(f'O número 3 está na posição {tupla.index(3)}')
print('-=' * 15)

#numeros pares
count1 = 0
for d in tupla:
    if d % 2 == 0:
        count1 += 1
        print(f'Os valores pares digitados foram {count}')
print('-=' * 15)