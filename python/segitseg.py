import random


def felezo(jo_valasz):

    valaszok = ["a", "b", "c", "d"]
    helytelenvalaszok = []
    for i in valaszok:
        if i != jo_valasz:
            helytelenvalaszok.append(i)

    veletlen = helytelenvalaszok[random.randint(0, 2)]
    return (jo_valasz, veletlen)  # randomizálni


print(felezo("a"))
