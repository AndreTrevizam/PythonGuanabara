ano_nasc = int(input('Digite seu ano de nascimento: '))

idade = 2024 - ano_nasc

if idade < 18:
    print(f'Você tem {idade}, você ainda vai se alistar ao serviço militar.')
elif idade == 18:
    print(f'Você precisa se alistar esse ano!')
elif idade > 18:
    print(f'Você tem {idade} anos! Seu tempo de alistamento já passou!')