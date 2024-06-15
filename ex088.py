import random
import time

print('---------------------------')
print('     JOGA NA MEGA SENA     ')
print('---------------------------')

num_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'-=-=-= SORTEANDO {num_jogos} JOGOS -=-=-=')

princ = []
copia = []

for i in range(num_jogos):
    num_aleatorio = random.sample(range(1,61), 6)
    princ.append(num_aleatorio)
    copia.append(princ[:])
    princ.clear()

cont = 1
for n in copia:
    print(f'Jogo {cont}: {n[0]}')
    cont += 1
    time.sleep(0.5)

print(f'-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')