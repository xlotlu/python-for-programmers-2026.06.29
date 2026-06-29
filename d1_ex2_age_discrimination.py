# Exercițiu
# 1. Cerem vârsta utilizatorului
# 2. a) Dacă vârsta este < 18,
#       print("Ești prea tânăr")
#    b) Dacă vârsta este >= 60,
#       print("Ești prea în vârstă")
#    c) Toate celelalte cazuri,
#       print("Ai vârsta potrivită")

# știind doar if & else,
# puteți rezolva problema?

age = input("Vârsta ta? ")
age = int(age)

# if age < 18:
#     print("Ești prea tânăr")
# else:
#     if age >= 60:
#         print("Ești prea în vârstă")
#     else:
#         print("Ai vârsta potrivită")



if age < 18:
    print("Ești prea tânăr")
elif age >= 60:
    print("Ești prea în vârstă")
    print("etc")
else:
    print("Ai vârsta potrivită")


# # if statement:

# # forma 1
# if cond1:
#     statement1

# # forma 2
# if cond1:
#     statement1
# else:
#     statement_alt

# # forma 3
# if cond1:
#     statement1
# elif cond2:
#     statement2
# # elif ...

# # forma 4
# if cond1:
#     statement1
# elif cond2:
#     statement2
# elif cond3:
#     statement3
# # ...
# else:
#     statement_alt
