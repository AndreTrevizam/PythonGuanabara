soma = 0
for c in range(6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma += num
print(soma)