from time import sleep

for c in range(10, -1, -1):
    print(f'Contagem para os fogos de artifício: {c} segundos')
    sleep(1)
print('BOOOOM')