nota = float(input('Digite a nota:'))
nota2 = float(input('Digite a nota:'))

media = (nota + nota2) / 2

if media < 5:
    print(f'Sua média é de {media:.1f}! Você foi reprovado')
elif media >= 5 and media <= 6.9:
    print(f'Sua média é de {media:.1f}! Você está de recuperação')
elif media >= 7:
    print(f'Sua média é de {media:.1f}! Você foi aprovado')