from typing import Dict, List

class Library:
    def __init__(self, ksiazki: Dict[str, str]) -> None:
        self.ksiazki = ksiazki

    def find_book(self, isbn: str) -> str:
        if isbn in self.ksiazki:
            return self.ksiazki[isbn]
        else:
            return None
        
if __name__ == "__main__":
    ksiazki = {"12nm34m": "W pustyni i w puszczy",
               "2ndhx6s": "Dziady",
               "dnv74nd": "Lalka"}
    biblioteka = Library(ksiazki)
    isbn = input("Podaj numer ISBN ksiażki: ")
    tytul = biblioteka.find_book(isbn)
    if tytul:
        print(f"Książka o takim numerze ISBN znajduje się w biliotece i ma tytuł: {tytul}")
    else:
        print("Nie ma takiej ksiażki w bibliotece")