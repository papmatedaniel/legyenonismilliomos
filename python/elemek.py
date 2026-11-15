class Elemek:
    def __init__(self, sor):
        self.nehezseg: int = int(sor[0])
        self.kerdes: str = sor[1]
        self.a: str = sor[2]
        self.b: str = sor[3]
        self.c: str = sor[4]
        self.d: str = sor[5]
        self.valasz: str = sor[6]
        self.kategoria: str = sor[7]

    def __str__(self):
        return f"""Nehézség: {self.nehezseg}
                    Kérdés: {self.kerdes}
                    a): {self.a}
                    b): {self.b}
                    c): {self.c}
                    d: {self.d}
                    Válasz: {self.valasz}
                    Kategória: {self.kategoria}


"""


class DicsosegLista:
    def __init__(self, sor):

        (self.jatekosnev, self.nyeremeny, self.ido) = sor

    def __str__(self):
        return f"""jatekos: {self.jatekosnev}, EDDIG jutottál: {self.nyeremeny}, ido: {self.ido}"""
