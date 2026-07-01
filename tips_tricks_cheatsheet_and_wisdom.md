# Python is:

"self-documenting"
whitespace-sensitive

"duck typing": if it walks like a duck and quacks like a duck, it's good enough


# Essentials:

în Python totul este un obiect


funcția:
- primește un input (argumente)
- returnează un output (return value!)
- și/sau are side-effects (modifică starea sistemului)


în Python totul este o referință

# data types:

int
float
str

bool

list  # este mutabilă
tuple # immutable

range # data-type de sine stătător

notă: str, list & tuple sunt "sequences":
- sunt iterabile
- au o ordine dată
- sunt accesibile după index
- suportă operatorii + și *
  (deci și += și *= )
- toate suportă len()
- suportă operatorul in
- toate au metodele .count() și .index()


# statements:

del variabila
del variabila[item]

# essential debugging tools

print()
help()
type() # returnează data-type-ul
dir() # listează toate atributele

and the (pen)ultimate debugging tool:
în shell:

```
$ pip install ipdb
```

în python:

```
import ipdb
```

și la linia unde vrem să intrăm în execuție:

```
ipdb.set_trace()
```

# good to know:
PEP-8: the styleguide
https://peps.python.org/pep-0008/


# important exception types

SyntaxError
IndentationError

NameError       # când variabila nu este declarată
TypeError       # când amestecăm data-type-uri în mod invalid
                # când nu respectăm argumentele funcției

ValueError      # nu există valoarea căutată
                # argumentul primit are valoare invalidă

IndexError      # nu există indexul
AttributeError

# using VSCode

Ctrl+/       comment selection block
Ctrl+F5      run current file
Tab          indent selection
Shift+Tab    unindent selection

# wisdom

readability is king:
  - naming things (variables & functions)
  - sparse code (vs. dense)
  - algoritmi simplificați
  - funcții foarte specifice
  - comments, comments, comments


there are 2 very difficult problems in computing:
- naming things
- cache invalidation
- off-by-one errors


DRY = don't repeat yourself
