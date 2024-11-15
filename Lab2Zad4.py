import numpy as np
from functools import reduce

def wykonaj_operacje_na_macierzach(macierze, operacja):
    """
    Funkcja wykonuje określoną operację na liście macierzy.
    
    :param macierze: Lista macierzy, na których ma zostać wykonana operacja
    :param operacja: Typ operacji, może być 'dodawanie' lub 'mnożenie'
    :return: Wynik operacji na macierzach
    """
    if operacja == "dodawanie":
        operacja_func = lambda x, y: x + y
    elif operacja == "mnożenie":
        operacja_func = lambda x, y: np.dot(x, y)
    else:
        raise ValueError("Nieznana operacja! Dozwolone operacje: 'dodawanie' lub 'mnożenie'.")
    
    return reduce(operacja_func, macierze)

def main():

    macierz_a = np.array([[1, 2], [3, 4]])
    macierz_b = np.array([[5, 6], [7, 8]])
    macierz_c = np.array([[9, 10], [11, 12]])
    
    macierze = [macierz_a, macierz_b, macierz_c]
    
    operacja = "dodawanie"
    
    wynik = wykonaj_operacje_na_macierzach(macierze, operacja)
    
    print(f"Rezultat operacji '{operacja}':")
    print(wynik)

if __name__ == "__main__":
    main()
