import numpy as np

def pole_kwadratu(bok: float) -> float:
    return bok*bok 

def pole_prostokata(szerokosc: float, dlugosc: float) -> float:
    return szerokosc*dlugosc

def pole_kola(promien: float) -> float:
    return np.pi*promien**2