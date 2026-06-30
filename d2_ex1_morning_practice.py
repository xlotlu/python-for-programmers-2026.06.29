# 1. creați un string format din string-ul "tra la la"
# repetat de 7 ori.
"tra la la" * 7

# 2. obțineți partea întreagă a împărțirii lui 17 la 4.
17 // 4

# 3. obțineți restul împărțirii lui 17 la 4.
17 % 4

# 4. ridicați 8 la puterea a 3a.
8 ** 3

# 5. scrieți o funcție `cube(x)` ce returnează
# valoarea lui x ridicat la puterea a 3a.
def cube(x):
    return x ** 3

# 6. a) luați un număr întreg ca input de la utilizator.
#       dacă input-ul nu este număr întreg valid,
#       cereți din nou input().


def get_input_int(prompt="Enter a number: "):
    # maybe don't do this, because it's unreadable
    while not (num := input(prompt)).isdecimal():
        print("Error. Enter a valid number.")

    return int(num)

#    b) folosiți funcția cube() de mai sus pentru a calcula
#       cubul numărului, apoi faceți print unui string de forma
#       "Cubul numărului <number> este <num_cube>."

num = get_input_int()
cb = cube(num)

print("Cubul numărului " + str(num) + " este " + str(cb) + ".")
print(f"Cubul numărului {num} este {cb}.")


#7. printați toate numerele întregi de la 100 la 124
# folosind `for` și `range()`.
for x in range(100, 125):
    print(x)

#8. printați toate numerele întregi de la 100 la 124
# folosind `while`.
x = 100
while x < 125:
    print(x)
    x += 1

#9. dată fiind lista
lst = ["ala", "bala", "porto"]

# a) printați elementul de la indexul 2
print(lst[2])
# b) printați al 2lea element
print(lst[1])
# c) adăugați elementul "cala" la sfârșitul listei
lst.append("cala")
# d) ștergeți elementul de la indexul 0,
#    fără a îl returna (cu statement-ul `del`)
del lst[0]
# e) inserați la indexul 0 elementul "trala"
lst.insert(0, "trala")
# f) ștergeți elementul de la indexul 1,
#    returnându-l în același timp.
lst.pop(1)
# g) sortați lista alfabetic.
lst.sort()
