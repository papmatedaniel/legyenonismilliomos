import csv
import os
import random
import time

from dicslista import (
    dicsoseglistabeolvas,
    dicsoseglistakiirat,
    dicsoseglistamentes,
    dicsoseglistarendez,
)
from elemek import DicsosegLista, Elemek
from segitseg import felezo


def clear():
    """Képernyő törlése"""
    os.system("cls" if os.name == "nt" else "clear")


def beolvas():
    """Beolvassa, listaként<Elemek> adja vissza a filet"""
    lista = [[] for _ in range(15)]
    with open("loim.csv", "r", encoding="utf-8") as file:
        olvaso = csv.reader(file)
        next(olvaso)
        for sor in olvaso:
            elem = Elemek(sor)
            lista[elem.nehezseg - 1].append(elem)

    return lista


# valtozok, KONSTANSOK
nyeremenyek = [
    0,
    5000,
    10000,
    25000,
    50000,
    100000,
    200000,
    300000,
    500000,
    800000,
    1500000,
    3000000,
    5000000,
    10000000,
    20000000,
    40000000,
]


def kerdesgeneral(lista, kezdoszint):
    """Legenerál egy véletlen játékot"""
    return [random.choice(lista[i]) for i in range(kezdoszint - 1, 15)]


def jatekmenet(lista):
    """Végrehajtja a játékot, módtol függetlenül"""

    start_ido = time.time()
    utolsonehezseg = 0

    for i in lista:
        utolsonehezseg = i.nehezseg

        print(
            f"=== {utolsonehezseg}. KÉRDÉS | TÉT: {nyeremenyek[utolsonehezseg]} Ft ==="
        )
        print(f"Kategória: {i.kategoria}")
        print(f"Kérdés: {i.kerdes}\n")
        print(f"\ta) {i.a}")
        print(f"\tb) {i.b}")
        print(f"\tc) {i.c}")
        print(f"\td) {i.d}\n")
        # print(f"Jó megoldás: {i.valasz}")

        valasza = input(
            "Add meg a válaszodat (A, B, C, D) vagy (M - megállás): "
        ).upper()

        eltelt = int(time.time() - start_ido)
        ido = f"{eltelt // 60}:{eltelt % 60:02d}"

        if valasza == "M":  # megáll
            # adott szinthez kötött nyereményt kapja meg megállásnál
            return (nyeremenyek[utolsonehezseg - 1], ido)

        if valasza == "F":
            a, b = felezo(i.valasz)
            valasza = input(f"\tkét lehetséges opció: {a} - {b}: ").upper()

        if valasza != i.valasz:
            # utolso merfoldkovet adja vissza
            return (nyeremenyek[int((utolsonehezseg - 1) / 5) * 5], ido)

        if utolsonehezseg != 15:
            print("\nHelyes válasz! Jön a következő...")

    clear()
    print("Gratulálok, nyertél!")
    eltelt = int(time.time() - start_ido)
    ido = f"{eltelt // 60}:{eltelt % 60:02d}"
    return (nyeremenyek[utolsonehezseg], ido)


###===== Bekérések ====###


def nevbeker():
    """Bekéri a nevet"""
    return input("Add meg a neved: ")


def szintbeker():
    """Bekéri a nevet"""
    return int(input("\nAdd meg a kezdőszintet (1-15): "))


def fomenu():
    """Bekéri a főmenü inputjait"""
    print("=== LEGYEN ÖN IS MILLIOMOS ===")
    print("1. Játék indítása")
    print("2. Dicsőséglista")
    print("3. Kilépés")
    return int(input("\nVálasztás: "))


def jatektipus():
    """Játékmód kiválasztás"""
    print("=== JÁTÉKMÓD KIVÁLASZTÁSA ===")
    print("1. Normál játékmód")
    print("2. Egyedi nehézség")
    print("3. Vissza a főmenübe")
    return int(input("\nVálasztás: "))


def jatek():

    while True:
        clear()
        valasz = fomenu()

        if valasz == 3:
            clear()
            print("Köszönjük a játékot!")
            break

        if valasz == 2:
            clear()
            dicsoseglistakiirat(dicsoseglistarendez(dicsoseglistabeolvas()))
            input("\nNyomj Entert a visszalépéshez")

        if valasz == 1:
            clear()
            tipus = jatektipus()

            osszeskerdes = beolvas()

            if tipus == 1:
                nev = nevbeker()
                kerdesek = kerdesgeneral(osszeskerdes, 1)
                nyeremeny, ido = jatekmenet(kerdesek)

                print(f"\nJáték vége! Nyeremény: {nyeremeny} Ft | Idő: {ido}")
                uj_eredmeny = DicsosegLista([nev, str(nyeremeny), ido])
                dicsoseglistamentes(uj_eredmeny)
                input("\nNyomj Entert a visszalépéshez")

            if tipus == 2:
                szint = szintbeker()
                kerdesek = kerdesgeneral(osszeskerdes, szint)
                nyeremeny, ido = jatekmenet(kerdesek)

                print(f"\nJáték vége! Nyeremény: {nyeremeny} Ft | Idő: {ido}")
                input("\nNyomj Entert a visszalépéshez")

            if tipus == 3:
                continue


jatek()
