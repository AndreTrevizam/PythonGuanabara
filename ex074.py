from random import randint

numeros = []

for i in range(5):
    num = randint(0, 10)
    
    numeros.append(num)

print(tuple(numeros))

print(min(numeros))
print(max(numeros))