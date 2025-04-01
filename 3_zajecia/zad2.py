from typing import List

def average(liczby: List[float]) -> float:
    suma: float = 0
    for x in liczby:
        suma += x
    return suma/len(liczby)

if __name__ == "__main__":
    liczby: List[float] = [1, 12, 23.4, 1.2]
    print(f"Średnia z liczb {liczby} wynosi {average(liczby)}")