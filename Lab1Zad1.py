def podziel_paczki(wagi, max_waga):
    """
    Paczki na jak najmniejszą liczbę kursów.
    
    :param wagi: Lista wag paczek (list[int]).
    :param max_waga: Maksymalna waga, jaką może unieść kurier w jednym kursie (int).
    :return: Liczba kursów (int) , lista list paczek w każdym kursie (list[list[int]]).
    """
    wagi.sort(reverse=True)
    kursy = []
    
    for waga in wagi:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break
        if not dodano:
            kursy.append([waga])
    
    return len(kursy), kursy


def main():
    wagi = [2, 3, 7, 5, 6, 4]
    max_waga = 10

    liczba_kursow, kursy = podziel_paczki(wagi, max_waga)

    print("Liczba kursów:", liczba_kursow)
    print("Kursy:, Paczki:")
    for i, kurs in enumerate(kursy):
        print(f"{i + 1}: {kurs}")


if __name__ == "__main__":
    main()
