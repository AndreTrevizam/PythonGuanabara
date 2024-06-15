times_de_futebol = (
    "Flamengo",
    "Palmeiras",
    "Santos",
    "Corinthians",
    "São Paulo",
    "Internacional",
    "Grêmio",
    "Atlético Mineiro",
    "Cruzeiro",
    "Vasco da Gama",
    "Botafogo",
    "Fluminense",
    "Bahia",
    "Sport Recife",
    "Ceará",
    "Fortaleza",
    "Athletico Paranaense",
    "Goiás",
    "Chapecoense",
    "Avaí"
)

#apenas o 5 primeiros colocados
for times in times_de_futebol[:5]:
    print(times)
print('-=' * 15)

#os ultimos 4 colocados
for times in times_de_futebol[-4:]:
    print(times)
print('-=' * 15)

#uma lista com os times em ordem alfabetica
print(sorted(times_de_futebol))
print('-=' * 15)

#em que posiçao esta o time da chapecoense
for posicao, times in enumerate(times_de_futebol):
    if times == 'Chapecoense':
        print(f'{posicao + 1}. {times}')