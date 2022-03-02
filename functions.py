import literals as msg

def validate(msg, ini, fin):
    if fin is None:
        num = int(input(msg))
        while num < ini:
            num = int(input(msg))
    elif ini is None:
        num = int(input(msg))
        while num > fin:
            num = int(input(msg))
    elif ini is not None and fin is not None:
        num = int(input(msg))
        while num < ini or num > fin:
            num = int(input(msg))
    else:
        num = int(input(msg))
    return num


def mod_file(f):
    f = open(f, "w")
    x = validate(msg.MSG3, 1, None)
    for i in range(x):
        txt = input(msg.MSG4 + str(i + 1) + ": ")
        f.write(txt + "\n")
    f.close()

def direccio():
    f = input(msg.MSG1)
    if f[-4:] == '.txt':
        f = 'files/' + f
    else:
        f = 'files/' + f + '.txt'
    return f

def only_create(f):
    f = open(f, "w")
    f.close()


def read_file(f_name):
    f = open(f_name, "r")
    print()
    print(f.read())
    f.close()
