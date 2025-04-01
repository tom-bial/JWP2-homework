# Z dziedziczeniem czy kompozycją?
# Generator kodu?

class Asystent:
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

    def __str__(self):
        return f"{self.nazwa}, wersja {self.wersja}"

class AnalizaJezykowa:
    def __init__(self, kody_odpowiedzi):
        self.kody_odpowiedzi = kody_odpowiedzi

    def analizuj_zapytanie(self, zapytanie):
        #zapytanie = zapytanie.
        if "pogod" in zapytanie:
            return self.kody_odpowiedzi[0]
        elif "kawał" in zapytanie:
            return self.kody_odpowiedzi[1]
        else:
            return self.kody_odpowiedzi[2]
            
class GeneratorOdpowiedzi:
    def __init__(self, kody_odpowiedzi):
        self.kody_odpowiedzi = kody_odpowiedzi

    def generuj_odpowiedz(self, analiza):
        if analiza == self.kody_odpowiedzi[0]:
            return "Dzisiaj jest słonecznie"
        elif analiza == self.kody_odpowiedzi[1]:
            return "Z przyjemnością opowiem Ci kawał!"
        elif analiza == self.kody_odpowiedzi[3]:
            return "Niestety nie byłem w stanie rozpoznać twojego zapytania. Czy możesz sformułować je inaczej?"
        
class InteligentnyAsystent(Asystent):
    def __init__(self, nazwa, wersja):
        super().__init__(nazwa, wersja)
        self.kody_odpowiedzi = [1, 2, 3]
        self.analizator = AnalizaJezykowa(self.kody_odpowiedzi)
        self.generator = GeneratorOdpowiedzi(self.kody_odpowiedzi)

    def zapytaj(self, zapytanie):
        kod = self.analizator.analizuj_zapytanie(zapytanie)
        return self.generator.generuj_odpowiedz(kod)

        
if __name__ == "__main__":
    asystent = InteligentnyAsystent("AIRobot", 1.0)
    print(asystent)

    odpowiedz = asystent.zapytaj("Jaką mamy dziś pogodę?")
    print(odpowiedz)