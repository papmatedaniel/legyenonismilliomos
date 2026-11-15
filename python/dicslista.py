from elemek import DicsosegLista

###====Dicsőséglista kezelés===========###


def idomasodperckonverter(ido):
    """perc:másodperc -> másodperc"""
    perc, masodperc = ido.split(":")
    return int(perc) * 60 + int(masodperc)


def dicsoseglistabeolvas() -> list[DicsosegLista]:
    """beolvassa a dicsőséglistát tpye List<DicsosegLista>"""
    with open("dicsoseglista.csv", "r", encoding="utf-8") as file:
        return [DicsosegLista(i.split(",")) for i in file.read().split("\n")]


def dicsoseglistarendez(lista) -> list:
    """csökkenő buble sor: nyeremény, ha azonos idő alapján"""

    hossz = len(lista)
    for i in range(hossz):
        for j in range(i, hossz):
            if int(lista[i].nyeremeny) < int(lista[j].nyeremeny):
                lista[i], lista[j] = lista[j], lista[i]

            if int(lista[i].nyeremeny) != int(lista[j].nyeremeny):
                continue

            if idomasodperckonverter(lista[i].ido) > idomasodperckonverter(
                lista[j].ido
            ):
                lista[i], lista[j] = lista[j], lista[i]

    return lista


def dicsoseglistamentes(elem) -> None:
    """Új elemet ad hozzá a dicsőséglistához"""
    with open("dicsoseglista.csv", "a", encoding="utf-8") as file:
        file.writelines(f"\n{elem.jatekosnev},{elem.nyeremeny},{elem.ido}")


def dicsoseglistakiirat(lista) -> None:
    print("=" * 45)
    print("              DICSŐSÉGLISTA")
    print("=" * 45)
    for sorszam, i in enumerate(lista, 1):
        print(f"{sorszam}. {i}")
    print("=" * 45)
