ano_nasc = int(input('Digite o ano de nascimento do atleta: '))

idade = 2024 - ano_nasc

if idade <= 9:
    print(f'{idade} anos: Mirim')
elif idade > 9 and idade <= 14:
    print(f'{idade} anos: Infantil')
elif idade > 14 and idade <= 19:
    print(f'{idade} anos: Junior')
elif idade > 19 and idade <= 20:
    print(f'{idade} anos: Sênior')
elif idade > 20:
    print(f'{idade} anos: Master')