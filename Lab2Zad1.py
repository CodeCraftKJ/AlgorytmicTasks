import re
from collections import Counter

STOP_WORDS = {"i", "a", "w", "na", "do", "z", "to","co", "po", "też"}

def analizuj_tekst(tekst):
    """
    Funkcja do analizy tekstu
    
    :param tekst: Tekst do analizy (str).
    :return: Słownik z wynikami analizy.
    """
    akapity = tekst.split('\n')
    liczba_akapity = len(akapity)-2
    zdania = re.split(r'[.!?]', tekst)
    liczba_zdan = len([zdanie for zdanie in zdania if zdanie.strip() != ""])
    slowa = tekst.split()

    liczba_slow = len(slowa)

    slowa_bez_stop_words = [slowo for slowo in slowa if slowo not in STOP_WORDS]
    najczestsze_slowa = Counter(slowa_bez_stop_words).most_common(10)

    def odwroc_slowo(s):
        return s[::-1]

    slowa_odwrocone = map(lambda s: odwroc_slowo(s) if s.lower().startswith('a') else s, slowa)
    tekst_po_transformacji = ' '.join(slowa_odwrocone)

    return {
        "liczba_slow": liczba_slow,
        "liczba_zdan": liczba_zdan,
        "liczba_akapity": liczba_akapity,
        "najczestsze_slowa": najczestsze_slowa,
        "tekst_po_transformacji": tekst_po_transformacji
    }


def main():
    tekst = """
    Eara Eaaaaa eaaa. Eaaaaa eaaa. Eaoem. Ameno.
    Adon Dom Oeaaa Oeamm.
    DOm. Oam Omemonm Meonommmmm.
    """

    wyniki = analizuj_tekst(tekst)

    print("Liczba słów:", wyniki["liczba_slow"])
    print("Liczba zdań:", wyniki["liczba_zdan"])
    print("Liczba akapitów:", wyniki["liczba_akapity"])
    print("Najczęściej występujące słowa:", wyniki["najczestsze_slowa"])
    print("\nNowy Tekst:")
    print(wyniki["tekst_po_transformacji"])


if __name__ == "__main__":
    main()
