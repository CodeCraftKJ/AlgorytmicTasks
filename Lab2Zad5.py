def generuj_i_uruchom_kod(szablon, dane):
    """
    Funkcja generuje kod na podstawie szablonu i danych wejściowych, a następnie go uruchamia.
    
    :param szablon: Szablon kodu Pythona jako string, np. "def funkcja(x): return x + {zmienna}"
    :param dane: Słownik z danymi, które będą wstawiane do szablonu kodu
    :return: Wynik wykonania wygenerowanego kodu lub komunikat o błędzie
    """
    
    kod = szablon.format(**dane)
    
    try:
        compiled_code = compile(kod, '<string>', 'exec')
        
        exec(compiled_code)
        
        if 'funkcja' in dane:
            return dane.funkcja(dane['zmienna'])
        return "Kod wykonany"
    
    except Exception as e:
        return f"Błąd w kodzie: {e}"

def main():
    szablon = "def funkcja(x): return x + {zmienna}"
    
    dane = {'zmienna': 3}
    
    wynik = generuj_i_uruchom_kod(szablon, dane)
    
    print(wynik)

if __name__ == "__main__":
    main()
