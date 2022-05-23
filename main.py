


class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

class Egzemplarz:
    def __init__(self, rok_wydania, wypozyczony):
        self.rok_wydania = rok_wydania
        self.wypozyczony = wypozyczony

class Czytelnik:
    def __init__(self, nazwisko):
        self.nazwisko = nazwisko

class Biblioteka:
  
    lista_ksiazek = []
    lista_egzemplarzy = []
    lista_krotek = []
    lista_ostateczna = []
    czy_jest_na_liscie = False

    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen = limit_wypozyczen

    def sortuj(self, e):
        return e['tytul']

    def dostepne_egzemplarze(self):

        for ksiazka in self.lista_ksiazek:
            for egzemplarze in self.lista_egzemplarzy:
                if egzemplarze.tytul == ksiazka.tytul and egzemplarze.autor == ksiazka.autor:
                    self.czy_jest_na_liscie = True

            if not self.czy_jest_na_liscie:
                self.lista_ostateczna.append({'tytul': ksiazka.tytul, 'autor': ksiazka.autor, 'ilosc_egzemplarzy': self.liczEgzemplarze(ksiazka)})
                self.czy_jest_na_liscie = False
                self.lista_egzemplarzy.append(ksiazka)

            self.czy_jest_na_liscie = False
            
        self.lista_ostateczna.sort(key=self.sortuj)
        for lista in self.lista_ostateczna:
            print("('" + lista['tytul'].strip() + "'" + ", " + "'" + lista['autor'].strip() + "', " + lista['ilosc_egzemplarzy'].strip() + ")")

    def dodaj_egzemplarz_ksiazki(self, ksiazka):
        self.lista_ksiazek.append(ksiazka)

    def liczEgzemplarze(self, aktualna_ksiazka):
        wynik = 0
        for ksiazka in self.lista_ksiazek:
            if aktualna_ksiazka.tytul == ksiazka.tytul and aktualna_ksiazka.autor == ksiazka.autor:
                wynik += 1

        return str(wynik)


n = int(input()) #liczba egzemplarzy 
lista_ksiazek = [eval(input().strip()) for ksiazka in range(n)]
biblioteka = Biblioteka(10)

for ksiazka_pozycja in lista_ksiazek:
    ksiazka = Ksiazka(ksiazka_pozycja[0], ksiazka_pozycja[1], ksiazka_pozycja[2])
    biblioteka.dodaj_egzemplarz_ksiazki(ksiazka)

biblioteka.dostepne_egzemplarze()
