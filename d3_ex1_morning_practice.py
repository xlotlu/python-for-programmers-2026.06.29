# 1. Dat fiind string-ul

s = "Bună dimineața, ce plăcut și răcoros este afară!"

# faceți print
# - primelor 4 caractere
s[:4]

# - ultimelor 6 caractere
s[-6:]

# - caracterelor de la început până la ultimele 6
s[:-6]

# - caracterelor dintre index-ul 16 și 25, inclusiv
s[16:26]


# 2. Întrebare:
# știind că sintaxa completă a funcției `range()` este
# range(start, stop, step) unde `step` are default 1,
# cum iterați în ordine inversă de la 20 la 0?

for x in range(20, -1, -1):
    print(x)


# 3. Știind că sintaxa completă de slicing este
# iterabil[start:stop:step] unde `step` are default 1,
# printați str-ul `s` de la coadă la cap.
s[::-1]



######


# 4. Dat fiind numele de coloană
c = "####Name####"
# obțineți numele de coloană fără caracterele
# de padding.
c.strip('#')

# 5. Dat fiind capul de tabel
h = "|####Name # etc####|#Age#|#####Address#####|"
# obțineți o listă cu numele coloanelor.
#
# (facem: split, limităm după indecși (slicing), cleanup, construim listă)

cols = h.split("|")

columns = []
for c in cols[1:-1]:
    clean = c.strip('#')
    columns.append(clean)

# cu list comprehension:

print(
    [
        c.strip('#')
        for c in cols[1:-1]
    ]
)


# 6. Scrieți o funcție ce replică fncționalitatea
# lui `str.startswith()`

def startswith(s, substr):
    return s[:len(substr)] == substr


# 7. [opțional pentru cine a terminat repede]
# Scrieți o funcție ce replică funcționalitatea
# lui `str.removesuffix()`

def removesuffix(s, suffix):
    slen = len(suffix)
    if s[-slen:] == suffix:
        return s[:-slen]
    return s


# 8. [opțional]
# Scrieți o funcție
def padint(number, length):
    pass
# ce primind un număr întreg îl prefixează cu zero-uri
# până atinge lungimea dată.
# ex: padint(25, 4) --> "0025"
#
# faceți asta low-level, algoritmic, ignorând
# că există metodele `.rjust()` / `.zfill()`

def padint(number: int, length: int) -> str:
    # vom avea nevoie de număr întotdeauna ca string
    num = str(number)

    # verificăm lungimea numărului ca string
    nlen = len(num)
    # dacă numărul are lungime mai mare decât length
    if nlen > length:
        return num
    # în celelealte cazuri, avem de lipit
    # un număr de zero-uri la stânga nr.-ului inițial

    # calculăm diferența dintre `length` și lungimea nr.-ului
    diff = length - nlen
    # ne generăm numărul de zero-uri necesar
    pad = str(0) * diff

    return pad + num
