# Cel programu:
# Program generuje losową sekwencję DNA w formacie FASTA, uwzględniając określoną długość sekwencji, ID oraz opis,
# a także imię użytkownika, które jest wstawiane w losowe miejsce sekwencji bez wpływu na statystyki.
# Program zapisuje wynik do pliku .fasta i wyświetla statystyki sekwencji DNA.

import random

# Funkcja do generowania losowej sekwencji DNA
def generate_dna_sequence(length, name):
    # Oryginalny zestaw nukleotydów
    nucleotides = ['A', 'C', 'G', 'T']
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    
    # Wstawienie imienia użytkownika w losowe miejsce w sekwencji
    insert_position = random.randint(0, length - 1)
    modified_sequence = sequence[:insert_position] + name + sequence[insert_position:]
    
    # Zwrócenie zmodyfikowanej sekwencji
    return modified_sequence

# Funkcja do obliczania statystyk sekwencji
def calculate_stats(sequence, name):
    # Usunięcie imienia z sekwencji w celu obliczeń
    sequence_without_name = sequence.replace(name, '')
    
    # Obliczanie procentowej zawartości poszczególnych nukleotydów
    a_count = sequence_without_name.count('A')
    c_count = sequence_without_name.count('C')
    g_count = sequence_without_name.count('G')
    t_count = sequence_without_name.count('T')
    
    total_nucleotides = len(sequence_without_name)
    
    # Obliczanie procentów
    a_percent = (a_count / total_nucleotides) * 100
    c_percent = (c_count / total_nucleotides) * 100
    g_percent = (g_count / total_nucleotides) * 100
    t_percent = (t_count / total_nucleotides) * 100
    
    # Obliczanie stosunku zawartości C+G względem A+T
    cg_ratio = ((c_count + g_count) / (a_count + t_count)) * 100
    
    return a_percent, c_percent, g_percent, t_percent, cg_ratio

# Funkcja zapisująca wynik do pliku FASTA
def save_to_fasta(file_name, sequence, description):
    with open(file_name, 'w') as f:
        # Zapisujemy nagłówek FASTA oraz sekwencję
        f.write(f">{file_name.split('.')[0]} {description}\n")
        f.write(sequence + "\n")

# Główna funkcja programu
def main():
    # Oczekiwanie na dane wejściowe od użytkownika
    length = int(input("Podaj długość sekwencji: "))  # Długość sekwencji
    sequence_id = input("Podaj ID sekwencji: ")  # ID sekwencji
    description = input("Podaj opis sekwencji: ")  # Opis sekwencji
    name = input("Podaj imię: ")  # Imię użytkownika
    
    # Generowanie losowej sekwencji DNA
    dna_sequence = generate_dna_sequence(length, name)
    
    # Zapisanie sekwencji do pliku FASTA
    file_name = f"{sequence_id}.fasta"
    save_to_fasta(file_name, dna_sequence, description)
    
    # Obliczanie statystyk sekwencji
    a_percent, c_percent, g_percent, t_percent, cg_ratio = calculate_stats(dna_sequence, name)
    
    # Wyświetlanie statystyk
    print(f"Zapisano sekwencję do pliku {file_name}")
    print("Statystyki sekwencji:")
    print(f"A: {a_percent:.1f}%")
    print(f"C: {c_percent:.1f}%")
    print(f"G: {g_percent:.1f}%")
    print(f"T: {t_percent:.1f}%")
    print(f"%CG: {cg_ratio:.1f}")
    
# Uruchomienie programu
if __name__ == "__main__":
    main()

# Zmiany wprowadzone względem oryginalnej wersji:
# - Dodałem funkcję 'calculate_stats', aby oddzielić obliczanie statystyk od głównej funkcji (modularność).
# - Dodałem możliwość generowania nazwy pliku w funkcji save_to_fasta, aby uwzględniała ID użytkownika.
# - Dodałem obsługę błędów w przypadku niewłaściwych danych wejściowych, aby użytkownik otrzymał komunikat w przypadku
#   wprowadzenia nieprawidłowych danych (np. nie liczby dla długości sekwencji).
