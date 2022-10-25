name = ""

def normalize(name):

    name = input()
    name = name.replace('é', 'e')
    name = name.replace('ë', 'e')
    name = name.replace('á', 'a')
    name = name.replace('å', 'aa')
    name = name.replace('œ', 'oe')
    name = name.replace('æ', 'ae')
    return name

print(normalize(name))