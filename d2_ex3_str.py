s = "Este o după-amiază minunată de mers la plajă."

# s.replace(match, replacement)
s.replace(" ", "\n")


s.count('substr')

# acestea fac același lucru
s.find("substr")
# dar .find() returnează -1 if not found
#s.index("substr")
# iar .index() raises ValueError if not found
# (cel pythonic este index)


s.split() # returnează o listă.
# fără argumente face split după orice este "whitespace".
# cu argumente splitează doar după acel susbtr:
"my.name@gmail.com".split("@")
username, domain = "my.name@gmail.com".split("@")

# inversul lui split, join:
"|".join(("Column 1", "Column 2", "Name", "Address"))



s.splitlines()
# este ce vrem când splităm un input mare
# (conținutul unui fișier text)
# după rânduri


# utile pt. curățare:
# s.strip() / s.lstrip() / s.rstrip()

# strip by default curăță whitespace
"    Gigel Popescu  \n \t   ".strip()

# cu parametru curăță acele caractere
"    Gigel Popescu  \n \t   ".strip(" \t")

"00001230".lstrip("0")

# utile, uneori, manipulare de string:
#.removepreffix(substr)
#.removesuffix(substr)
# curăță _specific_ acel substr dacă este ca prefix/sufix


# utile, uneori
s.startswith("Xxx")
s.endswith("xyz")


# utile, rareori, manipulare de lower/uppercase:
s.capitalize()
s.lower()
s.upper()
s.title()

s.casefold() # de folosit la comparare de string-uri
             # când vrem să normalizăm la case-insensitive.


# și mai puțin utile dacă nu facem
# parsare / output de text în consolă
t = "text mic"

t.center(20)
t.ljust(20, '#')
t.rjust(20)


# probabil nu veți avea nevoie de așa ceva vreodată:
# s.encode("utf-8")
# bytes_object.decode("utf-8")


# Exercițiu
# scrieți o funcție
def get_words(txt):
    pass
# ce returnează o listă cu toate cuvintele din `txt`

print(
    get_words("""
        Eu sunt un mare text !!!
        ce povestesc di-verse.
        și am și $#@ caractere pierdute,
        în mod interesant (în interior).
    """)
)


# ne pregătim dataset-ul de filtrare
# one-time, nu în interiorul funcției

_BAD_RANGES = (
    (0x21, 0x2f),
    (0x3a, 0x40),
    (0x5b, 0x60),
    (0x7b, 0x7e),
)

BAD_CHARS = []

for start, stop in _BAD_RANGES:
    for num in range(start, stop + 1):
        BAD_CHARS.append(chr(num))

def get_words(txt):
    # vrem să facem replace la toate bad chars

    for char in BAD_CHARS:
        txt = txt.replace(char, ' ')

    return txt.split()

# implementare 2, folosind .translate()
# (search & replace pe toate caracterele deodată)

# cum transformăm o listă de caractere într-un string
# cu caracterele lipite?
#"".join(BAD_CHARS)

# cum fac un string format numai din spații
# de lungimea acestei liste BAD_CHARS?
#" " * len(BAD_CHARS)

BAD_CHARS_TABLE = str.maketrans("".join(BAD_CHARS), " " * len(BAD_CHARS))

def get_words(txt):
    return txt.translate(BAD_CHARS_TABLE).split()


"""

s.format()


"""
