# while:

# pattern 1:
# ne ocupăm în interiorul while-ului
# să transformăm condiția în False
x = 5
while x < 10:
    print("x este", x)
    x += 1
    sleep(1)


# pattern 2:
# ne ocupăm în interiorul while-ului
# să facem break explicit
x = 5
while True:
    if x >= 10:
        break
    print(x)
    x += 1



# Exercițiu:
# scrieți o funcție
def get_input_int():
    pass
# ce promptează în mod repetat utilizatorul
# până acesta face input unei valori întregi.
#
# când această condiție a fost îndeplinită,
# funcția face return valorii,
# cu data-type int.

# sosul secret:
# str-urile au metoda .isdecimal()

def get_input_int(prompt="Enter a number: "):
    while True:
        x = input(prompt)
        if x.isdecimal():
            # this is valid input
            return int(x)
        else:
            # this is invalid input,
            # we'll keep nagging the user
            print("Error. Enter a valid number.")

v = get_input_int("Age? ")
print(v, type(v))


# Exercițiu:
# scrieți o funcție
def get_password(prompt="Enter a password"):
    pass

# ce promptează în mod repetat utilizatorul
# până acesta face input unei parole valide.
#
# o parolă validă = un string cu cel puțin 3 caractere.


# v1: cu while True
def get_password(prompt="Enter a password: "):
    while True:
        password = input(prompt)
        if len(password) >= 3:
            return password # early exit
        
        print("eroare")

# v2: cu condiție ce se schimbă
def get_password(prompt="Enter a password: "):
    # the "walrus operator" does assignment
    # inside conditional statements
    while len(pwd := input(prompt)) < 3:
        print(f"Parola introdusa e prea scurta")

    return pwd
