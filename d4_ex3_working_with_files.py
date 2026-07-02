fp = open("data/it-was.txt", encoding="utf-8")

# 2 ways to read the contents:

# a)
content = fp.read()
print(content)

fp.seek(0)

# b)

for line in fp:
    print(line)


# example pattern
# when needing to close a file manually

def do_something_with(txt):
    return 1 / 0

fp = open("data/it-was.txt", encoding="utf-8")
# operează pe fișier
contents = fp.read()
do_something_with(contents)
fp.close()


# let's fix this:

fp = open("data/it-was.txt", encoding="utf-8")

try:
    contents = fp.read()
    do_something_with(contents)
#except Exception as e:
#    print("there was an error:", type(e), e)
finally:
    fp.close()


# nu mai este cazul de așa ceva,
# pentru că s-au inventat "context managers"

with open("data/it-was.txt", encoding="utf-8") as fp:
    contents = fp.read()
    do_something_with(contents)


# Exercițiu:
# scrieți o funcție
def grep(filename, match, insensitive=False):
    pass
# ce printează toate liniile din fișierul
# `filename` ce conțin substring-ul `match`

def grep(filename, match, insensitive=False):
    if insensitive:
        match = match.lower()

    with open(filename, 'r', encoding="utf-8") as fp:
        for line in fp:
            if insensitive:
                line = line.lower()

            if match in line:
                print(line.removesuffix("\n"))
