import random

# Cel programu: Program generuje losową sekwencję DNA w formacie FASTA
# Kontekst zastosowania: Użyteczny w bioinformatyce, szczególnie w tworzeniu fikcyjnych danych DNA do testowania algorytmów.

# Funkcja do generowania losowej sekwencji DNA
def generuj_sekwencje(dlugosc):
    # Możliwe nukleotydy
    nukleotydy = ['A', 'C', 'G', 'T']
    
    # Generowanie losowej sekwencji
    sekwencja = ''.join(random.choice(nukleotydy) for _ in range(dlugosc))
    
    return sekwencja

# Funkcja do obliczania statystyk sekwencji
def oblicz_statystyki(sekwencja, imie):
    # Wstawianie imienia w losowe miejsce w sekwencji
    miejsce = random.randint(0, len(sekwencja))
    sekwencja_z_imieniem = sekwencja[:miejsce] + imie + sekwencja[miejsce:]
    
    # Obliczanie zawartości nukleotydów
    a_count = sekwencja_z_imieniem.count('A')
    c_count = sekwencja_z_imieniem.count('C')
    g_count = sekwencja_z_imieniem.count('G')
    t_count = sekwencja_z_imieniem.count('T')
    
    # Obliczanie statystyk procentowych
    dlugosc_sekwencji = len(sekwencja_z_imieniem)
    a_percent = (a_count / dlugosc_sekwencji) * 100
    c_percent = (c_count / dlugosc_sekwencji) * 100
    g_percent = (g_count / dlugosc_sekwencji) * 100
    t_percent = (t_count / dlugosc_sekwencji) * 100
    
    # Obliczanie stosunku C+G do A+T
    cg_percent = (c_count + g_count) / (a_count + t_count) * 100
    
    # Wyświetlanie statystyk
    print(f"Statystyki sekwencji:")
    print(f"A: {a_percent:.1f}%")
    print(f"C: {c_percent:.1f}%")
    print(f"G: {g_percent:.1f}%")
    print(f"T: {t_percent:.1f}%")
    print(f"%CG: {cg_percent:.1f}")
    
    # Zwrócenie zmodyfikowanej sekwencji
    return sekwencja_z_imieniem

# Funkcja zapisująca sekwencję do pliku FASTA
def zapisz_do_pliku(id_sekwencji, opis, sekwencja):
    # Zapis do pliku o nazwie ID sekwencji
    # ORIGINAL: 
    # with open(f"{id_sekwencji}.fasta", "w") as file:
    # file.write(f">{id_sekwencji} {opis}\n")
    # file.write(sekwencja)
    # MODIFIED (dodanie obsługi błędu)

    try:
        with open(f"{id_sekwencji}.fasta", "w") as file:
            file.write(f">{id_sekwencji} {opis}\n")
            file.write(sekwencja)
    except IOError as e:
        print(f"Nie udało się zapisać do pliku: {e}")

# Główna funkcja programu
def main():
    # Pobieranie danych wejściowych od użytkownika
    # ORIGINAL:
    # dlugosc = int(input("Podaj długość sekwencji: "))
    # MODIFIED (dodanie walidacji):
    while True:
        try:
            dlugosc = int(input("Podaj długość sekwencji: "))
            if dlugosc <= 0:
                raise ValueError("Długość musi być liczbą dodatnią!")
            break
        except ValueError as e:
            print(e)

    # ORIGINAL:
    # id_sekwencji = input("Podaj ID sekwencji: ")
    # MODIFIED (dodanie walidacji ID - tylko litery i cyfry):
    while True:
        id_sekwencji = input("Podaj ID sekwencji (litery i cyfry): ")
        if id_sekwencji.isalnum():  # Sprawdzenie, czy ID zawiera tylko litery i cyfry
            break
        else:
            print("ID sekwencji może zawierać tylko litery i cyfry.")
    
    opis = input("Podaj opis sekwencji: ")
    imie = input("Podaj imię: ")

    # Generowanie losowej sekwencji
    sekwencja = generuj_sekwencje(dlugosc)
    
    # Obliczanie statystyk i wstawianie imienia
    sekwencja_z_imieniem = oblicz_statystyki(sekwencja, imie)
    
    # Zapisywanie do pliku
    zapisz_do_pliku(id_sekwencji, opis, sekwencja_z_imieniem)
    
    # Potwierdzenie zapisania do pliku
    print(f"Sekwencja została zapisana do pliku {id_sekwencji}.fasta")

if __name__ == "__main__":
    main()
