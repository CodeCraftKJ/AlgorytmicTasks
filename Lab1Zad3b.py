def optymalizacja(zadania):
    """
    Optymalizacja rozmieszczenia zadań za pomocą podejścia proceduralnego.
    
    :param zadania: Lista zadań w formacie [(czas, nagroda)].
    :return: Optymalna kolejność zadań i całkowity czas oczekiwania.
    """
    zadania.sort(key=lambda x: x[0])
    
    calkowity_czas = 0
    czas_akumulowany = 0
    for czas, _ in zadania:
        czas_akumulowany += czas
        calkowity_czas += czas_akumulowany

    return zadania, calkowity_czas


def main():

    zadania = [(3, 50), (1, 20), (2, 30), (4, 60)]
    opt_kolejnosc, czas_oczekiwania = optymalizacja(zadania)
    
    print("Optymalna kolejność zadań:", opt_kolejnosc)
    print("Całkowity czas oczekiwania:", czas_oczekiwania)


if __name__ == "__main__":
    main()