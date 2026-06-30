#1. Scrieți o funcție
def get_greeting(hour: int) -> str:
    pass
# ce returnează unul din stringurile:
# între 5 și 10: "Bună dimineața"
# între 10 și 18: "Bună ziua"
# între 18 și 22: "Bună seara"
# între 22 și 5: "Noapte bună"

def get_greeting(hour: int) -> str:
    #hour = int(hour)
    # ^^ așa ceva facem doar dacă e responsabilitatea acestui cod
    # să sanitizeze datele (adică să ne asigurăm că au data-type corect).
    # când:
    #  - interacționăm cu: utilizatorul (via input, formular web)
    #  - citim date dintr-un fișier format text (ex: csv)

    if hour >= 5 and hour < 10:
        return "Buna dimineata"
    elif hour >= 10 and hour < 18:
        return "Buna ziua"
    elif hour >= 18 and hour < 22:
        return "Buna seara"
    elif (hour >= 22 and hour < 24) or (hour >= 0 and hour < 5):
        return "Noapte buna"
    else:
        # input was invalid
        raise ValueError(f"Invalid hour: {hour}")

# v2, complet echivalent
def get_greeting(hour: int) -> str:
    if 5 <= hour < 10:
        return "Buna dimineata"
    elif 10 <= hour < 18:
        return "Buna ziua"
    elif 18 <= hour < 22:
        return "Buna seara"
    elif (22 <= hour < 24) or (0 <= hour < 5):
        return "Noapte buna"
    else:
        # input was invalid
        raise ValueError(f"Invalid hour: {hour}")


# Scriem o funcție
def get_current_greeting() -> str:
    pass
# a zilei

# hints:
# from datetime import datetime
# datetime.now() # <-- returnează un obiect ora curentă
# acest obiect are atributul .hour

from datetime import datetime


def get_current_greeting():
    now = datetime.now()
    hour = now.hour
    return get_greeting(hour)


# Folosind funcția de mai sus,
# promptați utilizatorul pentru numele său
# și salutați-l potrivit pentru ora curentă a zilei.

#name = input("Cum te cheamă? ")
#print(get_current_greeting() + " " + name)
#print(f"{get_current_greeting()} {name}")



# Exercițiu:
# Creați o listă conținând pătratul numerelor
# de la 1 la 9.

patrate = []

for x in range(1, 10):
    ptr = x ** 2
    patrate.append(ptr)

#print(patrate)


# Exercițiu:
# Creați o listă conținând pătratul numerelor impare
# de la 1 la 21.

oddpatrate = []

for x in range(1, 22):
    if x % 2: # echivalent cu x % 2 != 0
        ptr = x ** 2
        oddpatrate.append(ptr)

#print(oddpatrate)


# Exercițiu:
# Dată fiind lista de tuple de forma (name, age)
candidates = [
    ('Mara', 28),
    ('George', 16),
    ('Dragoș', 42),
    ('Ana', 74),
    ('Mircea', 31),
    ('Carmen', 17),
    ('Andreea', 38),
    ('Vasi', 61),
]
# creați două liste noi, `accepted` și `rejected`,
# astfel încât persoanele cu vârsta între 18 și 60 de ani
# sunt accepted, iar celelalte rejected.


accepted = []
rejected = []

"""
for candidate in candidates:
    age = candidate[1]

    if 18 <= age <= 60:
        accepted.append(candidate)
    else:
        rejected.append(candidate)

print("Accepted candidates are: ", accepted)
print("Rejected candidates are: ", rejected)
"""

# Repetați exercițiul de mai sus
# (creați `accepted` și `rejected`)
# în timp ce consumați lista sursă.
# (adică la sfârșit `candidates` va fi o listă goală).

# Strategie:
#
# 1) putem consuma elementele din listă în mod repetat
#    folosind .pop()
#
# 2) știm că o listă goală în context boolean este False
#
# 3) ne vine vreo idee?

while candidates:
    candidate = candidates.pop()
    age = candidate[1]

    if 18 <= age <= 60:
        accepted.append(candidate)
    else:
        rejected.append(candidate)

print("Accepted candidates are: ", accepted)
print("Rejected candidates are: ", rejected)

print("Remaining:", candidates)


# Întrebare: contează ordinea?
# Dacă da:
#   - opțiunea 1: facem .reverse() în prealabil pe sursă
#   - opțiunea 2: facem .pop(0)

# [!] pe dataset-uri mari, .reverse() este preferabil
#     (deoarece face re-indexare o singură dată)
#     (în timp ce și .pop() face re-indexare, de fiecare dată)

