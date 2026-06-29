# input ---> funcție(input) ---> output

def numele_functiei():
    print("m-am rulat")
    return "o valoare"

def add(x, y):
    return x + y


# Exercițiu
# scrieți o funcție de forma
def filter_cities_300(cities):
    pass # placeholder, no-op, valid sintactic

# ce primind o listă de tuple de orașe
# returnează o listă nouă cu acele orașe filtrate
# (astfel încât să aibă distanța mai mică decât 300)

cts = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 400),
    ('Constanța', 225),
    ('Craiova', 230),
    ('Brașov', 180),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 600),
    ('Brăila', 200),
    ('Arad', 580),
    ('Sibiu', 275),
    ('Bacău', 300),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600),
    ('Buzău', 110),
    ('Satu Mare', 640),
    ('Suceava', 450),
]


def filter_cities_300(cities):
    # instanțiez
    o_lista_noua = []
    # iterez
    for city in cities:
        # filtrez
        if city[1] < 300:
            # acumulez
            o_lista_noua.append(city)
    # gata. returnez.
    return o_lista_noua

print(
    filter_cities_300(cts)
)


# Exercițiu
# scrieți o funcție
def filter_cities_by_distance(cities, distance):
    pass

# ce returnează o listă nouă cu acele orașe
# cu distanța mai mică decât `distance`

def filter_cities_by_distance(cities, distance):
    o_lista_noua = []
    for city in cities:
        if city[1] < distance:
            o_lista_noua.append(city)

    return o_lista_noua

print("»»",
    filter_cities_by_distance(cts, 200)
)

# Exercițiu
# scrieți o funcție
def filter_cities_by_letter(cities, letter):
    pass
# ce returnează o listă nouă cu acele orașe
# ce încep cu litera `letter`

# chain-uiți funcțiile
# `filter_cities_by_letter` și `filter_cities_by_distance`
# astfel încât să obțineți orașele ce încep cu litera "B"
# și sunt mai aproape de 300km.

def filter_cities_by_letter(cities, letter):
    out = []

    for city in cities:
        name = city[0]
        if name[0] == letter:
            out.append(city)

    return out


print('!',
    filter_cities_by_letter(
        filter_cities_by_distance(cts, 200),
        "B"
    )
)