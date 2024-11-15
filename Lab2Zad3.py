def analiza_danych(dane):
    """
    Zwraca największą liczbę numeryczną, najdłuższy napis oraz krotkę o największej liczbie elementów.
    
    :param dane: Lista zawierająca różne typy danych
    :return: Krotka zawierająca trzy wartości:
             - Największa liczba numeryczna,
             - Najdłuższy napis,
             - Krotka o największej liczbie elementów.
    """
    
    najwieksza_liczba = None
    najdluzszy_napis = None
    najwieksza_krotka = None

    for element in dane:
        if isinstance(element, (int, float)):
            if najwieksza_liczba is None or element > najwieksza_liczba:
                najwieksza_liczba = element
        
        elif isinstance(element, str):
            if najdluzszy_napis is None or len(element) > len(najdluzszy_napis):
                najdluzszy_napis = element

        elif isinstance(element, tuple):
            if najwieksza_krotka is None or len(element) > len(najwieksza_krotka):
                najwieksza_krotka = element

    return najwieksza_liczba, najdluzszy_napis, najwieksza_krotka

def main():
    dane = [42, "Aeoo eaoo emm", (1, 2, 3), [1, 2, 3], 2.99, "Kome", (4, 5), {"key": "value"}, 2]

    najwieksza_liczba, najdluzszy_napis, najwieksza_krotka = analiza_danych(dane)

    print(f"Największa liczba: {najwieksza_liczba}")
    print(f"Najdłuższy napis: {najdluzszy_napis}")
    print(f"Krotka o największej liczbie elementów: {najwieksza_krotka}")

if __name__ == "__main__":
    main()
