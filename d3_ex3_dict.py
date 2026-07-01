# dicționare

ages = {
    "Jane": 22,
    "Andrew": 44,
}

rows = {
    1: ['Jane', 20, ['reading', 'hiking', 'biking']],
    99: ['Dan', 34, ['painting', 'reading']],
}

friend = {
    'name': 'Jane',
    'age': 20,
    'hobbies': ['reading', 'hiking', 'biking']
}


# usecases cu colecții de date

d = {
    'Cluj-Napoca': 450,
    'Timișoara': 550,
    'Iași': 400,
    'Constanța': 225,
}

lst = [
    {
        'city': 'Cluj-Napoca',
        'distance': 450,
        'altitude': 62.5
    },
    {
        'city': 'Timișoara',
        'distance': 550,
        'altitude': 214.2
    },
]

sensor_data = [
    ('2026-07-01 15:18', 36.2),
    ('2026-07-01 15:20', 36.7),
]

sensor_data = {
    '2026-07-01 15:18': 36.2,
    '2026-07-01 15:20': 36.7,
}

# Exercițiu:
# transformați următoarea listă de tuple
# într-un dicționar nume: distanță

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

d = {}
for city, distance in cities:
    d[city] = distance

# dicționarul este iterabil, după chei:
for elem in d:
    print(elem)

# echivalent cu:
for elem in d.keys():
    print(elem)

# valorile:
for elem in d.values():
    print(elem)

# keys /and/ values:
for elem in d.items():
    print(elem)

# most commonly-found pattern
for k, v in d.items():
    print(k, v, sep=': ')

# dată fiind structura de date
friends = [
    ['Jane', 20, ['reading', 'hiking', 'biking']],
    ['Mike', 17, ['hiking', 'fishing']],
    ['Anna', 25, []],
    ['Sam', 40, ['playing guitar', 'knitting']],
    ['Dan', 34, ['painting', 'reading']],
    ['Gigel the Wise', 88, ['everything', 'knitting', 'sleeping']]
]
# construiți un dicționar
# ages = {name: age, name: age, ...}

ages = {}
for friend in friends:
    name = friend[0]
    age = friend[1]
    ages[name] = age

# sau, construind dicționarul dintr-un iterabil
# al cărui elemente sunt din cheie, valoare:
dict([(f[0], f[1]) for f in friends])

# sau, folosind dict comprehension:
{
    f[0]: f[1]
    for f in friends
}


# Exercițiu: având o structură de date de forma
# (name, age, city):
struct = ('Gigel', 20, 'Copenhaga')

# creați un dicționar cu cheile
# name, age, city
# și valorile respective

name, age, city = struct
d = {
    "name": name,
    "age" : age,
    "city" : city,
}

d = {
    "name": struct[0],
    "age": struct[1],
    "city": struct[2],
}

# sau, generalizând și folosind `zip()`:
columns = ('name', 'age', 'city')
d = dict(zip(columns, struct))
print(d)


# Exerciții:
# dat fiind raportul primit ca string cu acest format
s = """-----------------------------------
|    Name    | Age |     City     |
-----------------------------------
| Gigel      |  20 | Copenhaga    |
| Andrei     |  42 | București    |
| Georgiana  |  20 | Timișoara    |
| Andreea    |  20 | Constanța    |
| Carmencita |  20 | Satu Mare    |
| George     |  20 | Sfântu Gheor |
-----------------------------------"""


# scrieți o funcție `parse_report(txt)`
# ce returnează o listă de dicționare
# de forma
# [
#     {'Name': 'Gigel', 'Age': '20', 'City': 'Copenhaga'},
#     {'Name': 'Andrei', 'Age': '42', 'City': 'București'},
#     ...
# ]

# 1. ne facem o funcție helper
#    pentru a splita fiecare row în parte
def parse_row(txt):
    # dat fiind txt de forma
    # '| Gigel      |  20 | Copenhaga    |'
    # returnează o listă de forma:
    # ['Gigel', '20', 'Copenhaga']
    return [
        col.strip()
        for col in txt.split('|')[1:-1]
    ]

# 2. procesăm textul mare
def parse_report(txt):
    out = []

    lines = txt.splitlines()

    # we extract the column names
    columns = parse_row(lines[1])

    # we process each row
    for line in lines[3:-1]:
        row = parse_row(line)
        # d = {
        #     columns[0]: row[0],
        #     columns[1]: row[1],
        #     columns[2]: row[2],
        # }

        # much prettier:
        d = dict(zip(columns, row))
        out.append(d)

    return out

# cu list comprehension:
def parse_report(txt):
    lines = txt.splitlines()
    columns = parse_row(lines[1])

    # necitibil, poate preferați
    # varianta de mai sus
    return [
        dict(zip(columns, parse_row(line)))
        for line in lines[3:-1]
    ]

# hai să facem un dicționar
# unde cheile sunt numele,
# și valorile sunt dicționare

def parse_report_as_dict(txt):
    out = {}

    lines = txt.splitlines()
    columns = parse_row(lines[1])

    # we process each row
    for line in lines[3:-1]:
        row = parse_row(line)
        d = dict(zip(columns, row))

        #out[d['Name']] = d
        out[row[0]] = d

    return out