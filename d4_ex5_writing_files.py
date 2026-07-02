# Scrieți o funcție
def grepinto(srcfile, targetfile, match, insensitive=False):
    pass
# ce scrie în `targetfile` toate liniile din `srcfile`
# ce conțin substring-ul `match`

def grepinto(srcfile, targetfile, match, insensitive=False):
    if insensitive:
        match = match.lower()

    with open(targetfile, 'w', encoding="utf-8") as wf, open(srcfile, 'r', encoding="utf-8") as rf:
        for line in rf:
            if insensitive:
                line = line.lower()

            if match in line:
                wf.write(line)

# let's make it readable.
# a) line continuation character
def grepinto(srcfile, targetfile, match, insensitive=False):
    if insensitive:
        match = match.lower()

    with open(srcfile, 'r', encoding="utf-8") as rf, \
         open(targetfile, 'w', encoding="utf-8") as wf:
        for line in rf:
            if insensitive:
                line = line.lower()

            if match in line:
                wf.write(line)

# b) we gonna use brackets
def grepinto(srcfile, targetfile, match, insensitive=False):
    if insensitive:
        match = match.lower()

    with (
        open(srcfile, 'r', encoding="utf-8") as rf,
        open(targetfile, 'w', encoding="utf-8") as wf,
    ):
        for line in rf:
            if insensitive:
                line = line.lower()

            if match in line:
                wf.write(line)


# improve this and add a keyword argument that denies overwriting by default
def grepinto(srcfile, targetfile, match, insensitive=False, overwrite=False):
    if insensitive:
        match = match.lower()

    if overwrite:
        mode = 'w'
    else:
        mode = 'x'

    # perfect echivalent cu mai sus:
    mode = 'w' if overwrite else 'x'

    with (
        open(srcfile, 'r', encoding="utf-8") as rf,
        open(targetfile, mode, encoding="utf-8") as wf
    ):
        for line in rf:
            if insensitive:
                line = line.lower()

            if match in line:
                wf.write(line)
