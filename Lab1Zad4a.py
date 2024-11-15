def plecak_proceduralny(przedmioty, pojemnosc):
    """
    Rozwiązywanie problemu plecakowego metodą dynamiczną.
    
    :param przedmioty: Lista przedmiotów, gdzie każdy przedmiot to krotka (waga, wartość).
    :param pojemnosc: Maksymalna pojemność plecaka.
    :return: Maksymalna wartość, która może być zmieszczona w plecaku, oraz lista wybranych przedmiotów.
    """
    n = len(przedmioty)
    dp = [[0 for _ in range(pojemnosc + 1)] for _ in range(n + 1)]
    
    # Wypełnianie tablicy dp
    for i in range(1, n + 1):
        waga, wartosc = przedmioty[i - 1]
        for j in range(1, pojemnosc + 1):
            if waga <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - waga] + wartosc)
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Odtwarzanie wybranych przedmiotów
    wybrane_przedmioty = []
    j = pojemnosc
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            wybrane_przedmioty.append(przedmioty[i - 1])
            j -= przedmioty[i - 1][0]

    return dp[n][pojemnosc], wybrane_przedmioty


# Przykład użycia
przedmioty = [(2, 3), (3, 4), (4, 5), (5, 8)]
pojemnosc = 5

max_wartosc, wybrane = plecak_proceduralny(przedmioty, pojemnosc)
print(f"Maksymalna wartość: {max_wartosc}")
print(f"Wybrane przedmioty: {wybrane}")
