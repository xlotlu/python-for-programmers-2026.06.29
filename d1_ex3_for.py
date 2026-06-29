# for-ul iterează pe o colecție ("un iterabil")

# în Python _nu_ se iterează pe indexi,
# ci se iterează direct pe elementele colecției

collection = range(10)

for var in collection:
    print(var)

# range(end) # începe de la zero
# range(start, end) # start inclusiv, end exclusiv

for var in "un str":
    print(var)


lst = ["bla", "bli", "blu"]
for var in lst:
    print(var)


# un obiect are atribute și metode
# (metoda = o funcție ce acționează asupra obiectului)

#x = 2
#x.imag
#x.is_integer()

#y = 2.2
#y.real
#y.is_integer()


# Exercițiu:
# dată fiind lista de orașe:
cities = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
 'Craiova',
 'Brașov',
 'Galați',
 'Ploiești',
 'Oradea',
 'Brăila',
 'Arad',
 'Sibiu',
 'Bacău',
 'Târgu Mureș',
 'Baia Mare',
 'Buzău',
 'Satu Mare',
 'Suceava',
]

# faceți print orașelor care încep cu litera "B"
# hint: str-ul este accesibil după index


for city in cities:
    if city[0] == 'B':
        print(city)

# dată fiind lista de mai sus,
# creați o listă nouă ce conține
# orașele ce încep cu litera "B"

# inițializăm listă nouă
# și facem append

## Pattern de acumulare ##
# 1. inițializăm obiectul nou
lista_noua = []
# 2. iterăm prin sursa de date
for city in cities:
    # 3. filtrăm
    if city[0] == 'B':
        # 4. construim
        lista_noua.append(city)

# 5. suntem gata
print(lista_noua)

# Exercițiu:
# dată fiind lista
nums = [
    22, 46, 82, 15, 19,
]
# calculați media numerelor din listă

total = 0

for num in nums:
    #total = total + num
    total += num

media = total / len(nums)
print(media)


# Exercițiu:
# dată fiind lista de tuple de forma
# (name, distance)
cities = [
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
# printați orașele
# cu distanță mai mică decât 300

for city in cities:
    if city[1] < 300:
        print(city[0])

# Exercițiu:
# la fel ca mai sus,
# dar creați o listă nouă
# cu elementele a căror distanță
# este mai mică decât 300

close_cities = []
for city in cities:
    if city[1] < 300:
        close_cities.append(city)
