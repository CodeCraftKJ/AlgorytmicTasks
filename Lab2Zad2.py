import numpy as np

def operacje_na_macierzach(operacja_str, macierz_str1, macierz_str2=None):
    """
    Funkcja wykonuje operacje na macierzach zapisanych w formie stringów.
    """

    def string_do_macierzy(macierz_str):
        return np.array([list(map(int, row.split())) for row in macierz_str.strip().split('\n')])

    macierz1 = string_do_macierzy(macierz_str1)
    
    if macierz_str2:
        macierz2 = string_do_macierzy(macierz_str2)

    if "dodaj" in operacja_str:
        if macierz1.shape != macierz2.shape:
            raise ValueError("Macierze mają różne wymiary, nie można ich dodać!")
        return macierz1 + macierz2
    
    elif "pomnoz" in operacja_str:
        if macierz1.shape[1] != macierz2.shape[0]:
            raise ValueError("Niepoprawne wymiary macierzy do mnożenia!")
        return np.dot(macierz1, macierz2)
    
    elif "transponuj" in operacja_str:
        return np.transpose(macierz1)
    
    else:
        raise ValueError("Nieznana operacja!")

def main():
    macierz1_str = "1 2\n3 4"
    macierz2_str = "5 6\n7 8"

    operacja_dodaj = "dodaj"
    operacja_mnoz = "pomnoz"
    operacja_transponuj = "transponuj"

    print("Wynik dodawania:\n", operacje_na_macierzach(operacja_dodaj, macierz1_str, macierz2_str))
    print("Wynik mnożenia:\n", operacje_na_macierzach(operacja_mnoz, macierz1_str, macierz2_str))
    print("Wynik transponowania macierzy1:\n", operacje_na_macierzach(operacja_transponuj, macierz1_str))

if __name__ == "__main__":
    main()
