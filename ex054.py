count = 0
count1 = 0
for i in range(7):
    nasc = int(input('Em que ano você nasceu: '))
    idade = 2024 - nasc

    if idade < 18:
        count += 1
    else:
        count1 += 1
print(f'Temos {count} pessoas menor de idade')
print(f'Temos {count1} pessoas maior de idade')