# Exercițiu:
# cereți numele utilizatorului
# și salutați-l cu expresia
# "Salut <nume>"

# nume = input("Numele tău? ")

# print("Hello World")
# print("Salut " + nume)


# Exercițiu:
# Cereți două vârste
# și faceți output cu diferența lor

v1 = input("Age 1: ")
v2 = input("Age 2: ")

diff = int(v1) - int(v2)
print("Diferenta de varsta = ", diff)


# Exercițiu:
# Același exercițiu de mai sus, dar diferența
# output-ată să fie în totdeauna pozitivă:
# "Diferența de vârstă este <diff> ani"

# ideea 1: obținem valoarea absolută
#          folosind funcția abs()


diff = abs(diff)

print("Diferența de vârstă este " + str(diff) + " ani")

print(f"Diferența de vârstă este {diff} ani")

# ideea 2: folosim if

v1 = int(v1)
v2 = int(v2)

if v1 > v2:
    diff = v1 - v2
else:
    diff = v2 - v1

print(f"Diferența de vârstă este {diff} ani")
