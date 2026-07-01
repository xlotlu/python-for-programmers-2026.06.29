# Dată fiind structura de date
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# a) îmbătrâniți-o pe Jane cu 1 an.
# v1:
friends[0][1] = friends[0][1] + 1
# v2, mai frumos:
friends[0][1] += 1
# v3, acces via variabilă intermediară:
jane = friends[0]
jane[1] += 1  # merge pt. că jane este o referință la friends[0]



# diversiune:
# ce facem dacă unul din elemente nu are deloc(!) listă de hobby-uri?
# adică:
["Anna", 25]

# simulăm:
anna = friends[2]
del anna[2] # i-am șters hobby-urile

try:
    name, age, hobbies = friends[2]
except ValueError: # what we get when unpacking failed
    # this row is missing hobbies,
    # we have to create it explicitly
    hobbies = []
    # we set the variables, because the assignment above failed
    name, age = friends[2]
    # and finally we attach our hobbies list to the original data
    # (which works because averything is a reference)
    friends[2].append(hobbies)

# and now we can do hobbies.append() / hobbies.extend()


# b) Adăugați hobby-urilor Annei "reading" și "cooking"
anna = friends[2]
hobbies = anna[2]
hobbies.extend(["reading", "cooking"])

# warning:
# doing
anna[2] = anna[2] + ["reading", "cooking"]
# breaks the reference. it replaces the old hobbies with a new object!
# as oppsed to:
anna[2] += ["reading", "cooking"] # which is perfectly similar with .extend()


# c) Ștergeți-i lui Mike hobby-ul de la indexul 1
#del friends[1][2][1]

mike = friends[1]
hobbies = mike[2]
del hobbies[1]

# d) Adăugați un prieten nou:
f = ["Georgie", 22, ["reading", "cooking", "hiking"]]

friends.append(f)


######

# Scrieți trei funcții:
def get_by_name(contacts, name):
    pass
# ce primește ca parametru o listă de formatul `friends`
# și returnează primul element din listă ce are elem[0] == name
def get_by_name(contacts, name):
    for elem in contacts:
        if elem[0] == name:
            return elem


def find_by_age(contacts, min, max):
    pass
# ce returnează o listă similară cu cea de input,
# filtrată după contactele care au vârsta între `min` și `max`.
# (vârsta este pe poziția 1)


def find_by_age(contacts, min_age, max_age):
    new_list = []
    for friend in contacts:
       if min_age <= friend[1] <= max_age:
           new_list.append(friend)

    return new_list

print("»»", find_by_age(friends, 20,30))


def find_by_hobby(contacts, hobby):
    pass
# ce returnează o listă similară cu cea de input,
# filtrată după contactele care au `hobby` în lista de hobby-uri (index 2)


def find_by_hobby(contacts, hobby):
    result = []
    for contact in contacts:
        if hobby in contact[2]:
            result.append(contact)
    return result


# sintaxă de list comprehension completă:
# [elem for elem in iterable if condition]

# repetăm funcțiile de mai sus cu list comprehension

def find_by_age(contacts, min_age, max_age):
    return [
        friend
        for friend in contacts
        if min_age <= friend[1] <= max_age
    ]

def find_by_hobby(contacts, hobby):
    return [
        contact
        for contact in contacts
        if hobby in contact[2]
    ]

# let's chain them together
# căutăm prieteni între 20 și 40 de ani
# pentru un club de literatură

print(
    find_by_hobby(
        find_by_age(friends, 20, 40),
        'reading'
    )
)


# să găsim prietenii peste 40 de ani
# și le adăugăm hobby-ul "knitting"
find_by_age(friends, 40, 9999)

friends.append(['Gigel the Wise', 88, ["everything"]])

filtered_by_age = find_by_age(friends, 40, 9999)
for friend in filtered_by_age:
    friend[2].append("knitting")

# observăm cum operând asupra unei referințe la
# obiectele inițiale, schimbările pe care le-am
# făcut sunt vizibile în orice structură de date
# în care sunt folosite:

print(friends)
