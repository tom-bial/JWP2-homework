import numpy as np

def objetosc_szescianu(bok: float) -> float:
    return bok**3

def objetosc_prostopadloscianu(dlugosc: float, szerokosc: float, wysokosc: float) -> float:
    return dlugosc*szerokosc*wysokosc

def objetosc_kuli(promien: float) -> float:
    return (4/3)*np.pi*promien**3