#from pprint import pprint as print
from rich.pretty import pprint
from functools import partial


print = partial(pprint, indent_guides=False)


# Dată fiind lista de dicționare
friends = [
    {'name': 'Jane', 'age': 20, 'hobbies': ['reading', 'hiking', 'biking']},
    {'name': 'Mike', 'age': 17, 'hobbies': ['hiking', 'fishing']},
    {'name': 'Anna', 'age': 25, 'hobbies': []},
    {'name': 'Sam', 'age': 40, 'hobbies': ['playing guitar']},
    {'name': 'Dan', 'age': 34, 'hobbies': ['painting', 'reading']}
]

# și dat fiind dicționarul cu ocupații
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    "Sam": "boat captain",
    "Anna": "gardner",
}
# în care cheia este numele persoanei din dataset-ul `friends`,
# adăugați cheia "occupation" cu valoarea corespunzătoare fiecărui
# dicționar din sursă.
#
# La final lista `friends` urmqnd să aibă forma:
[
    {
        'name': 'Jane',
        'age': 20,
        'hobbies': ['reading', 'hiking', 'biking'],
        'occupation': 'nurse',
    },
    # ... etc.
]

# Strategie:
# 1. iterăm prin datasource-ul `friends`
#    --> fiecare element (persoana) este dicționarul
#        asupra căruia trebuie să operăm (aici adăugăm ocupația)
# 2. obținem numele persoanei din elementul curent
# 3. folosim numele drept cheie de lookup în `occupations`
# 4. obținem ocupația
# 5. adăugăm cheia "occupation" la elementul curent


for friend in friends:
    name = friend['name']
    occ = occupations[name]
    friend['occupation'] = occ

print(friends)

# Ne-am făcut un prieten nou:
friends.append({
    "name": "Jay",
    "age": 50,
    "hobbies": ["running", "hiking"],
})

# pattern-urile de tratat cu chei care nu există

# A) lookup cu if k in dct
for friend in friends:
    name = friend['name']

    if name not in occupations:
        continue # "early exit"

    occ = occupations[name]
    friend['occupation'] = occ

# B) try / except după KeyError
for friend in friends:
    name = friend['name']
    try:
        occ = occupations[name]
    except KeyError:
        continue
    
    friend['occupation'] = occ

# C) pentru pattern-urile când vrem
#    _întotdeauna_ o valoare, folosim `dict.get()`

# supposed task:
# să punem ocupație la toți oamenii din baza de date.
# dacă nu avem ocupație, completăm cu string-ul
# "UNKOWN"

for friend in friends:
    name = friend['name']
    occ = occupations.get(name, 'UNKNOWN')
    friend['occupation'] = occ

print(friends)


# Exercițiu:
# scrieți o funcție
def count_words(txt: str) -> dict:
    pass
# ce numără aparițiile fiecărui cuvânt din txt
# și returnează un dicționar de forma {cuvânt1: count1, ...}

# testați pe string-ul:
s = """
    It was the best of times,
    it was the worst of times,
    it was the age of wisdom,
    it was the age of foolishness,
    it was the epoch of belief,
    it was the epoch of incredulity,
    it was the season of light,
    it was the season of darkness,
    it was the spring of hope,
    it was the winter of despair.
"""

from d2_ex3_str import get_words

def count_words(txt: str) -> dict:
    out = {}

    for word in get_words(txt):   
        if word in out:
            out[word] += 1
        else:
            out[word] = 1

    return out

# alternativ
def count_words(txt):
    out = {}

    for word in get_words(txt):
        if word not in out:
            # we isolate the special case,
            # when the word doesn't yet exist
            out[word] = 0

        out[word] += 1
    return out

# alternativ 2

def count_words(txt, insensitive=False):
    out = {}

    if not insensitive:
        txt = txt.lower()

    for word in get_words(txt):
        old_count = out.get(word, 0)
        out[word] = old_count + 1

    return out

# dat fiind dicționarul 

cities = {
    'Cluj-Napoca': 450,
    'Timișoara': 550,
    'Iași': 400,
    'Constanța': 225,
    'Craiova': 230,
    'Brașov': 180,
    'Galați': 250,
    'Ploiești': 60,
    'Oradea': 600,
    'Brăila': 200,
    'Arad': 580,
    'Sibiu': 275,
    'Bacău': 300,
    'Târgu Mureș': 330,
    'Baia Mare': 600,
    'Buzău': 110,
    'Satu Mare': 640,
    'Suceava': 450
}

# creați o listă nouă cu numele orașelor ce au distanța
# mai mică decât 300 km,
# în timp ce consumați dicționarul.
#
# (la sfârșitul iterației dicționarul va fi gol,
# iar lisa populată cu valorile filtrate)


city_lst = []

while cities:
    name, dist = cities.popitem()
    if dist < 300:
        city_lst.append(name)

print(city_lst)