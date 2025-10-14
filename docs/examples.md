# Przykłady zastosowania metody ekspertów w prognozowaniu niezawodności

## Przykład 1: Obliczanie wartości A0 dla woltomierza cyfrowego

### Opis
Woltomierz cyfrowy ma zastąpić urządzenie o intensywności uszkodzeń wynoszącej Ā = 1,1 * 10^-5 [h^-1]. Współczynniki αe i αk obliczono na podstawie danych od ekspertów.

### Dane wejściowe
- Liczba mechaników (J_mech): 3
- Kmj: [1.3, 1.0, 1.2]
- Liczba elektroników (J_elec): 5
- Ng/N i Kg dla grupy elementów:
  - Grupa 1: [0.6, 2]
  - Grupa 2: [0.2, 4]
  - Grupa 3: [0.15, 1]
  - Grupa 4: [0.05, 1]

### Obliczenia
1. Oblicz Km:
   Km = (1/3) * (1.3 + 1.0 + 1.2) ≈ 1.16
2. Oblicz αk:
   αk = 1 / Km ≈ 0.86
3. Oblicz αe na podstawie αej:
   αe ≈ 0.46
4. Oblicz A0:
   A0 ≤ 1,1 * 10^-5 * 0.86 * 0.56 ≈ 0.435 * 10^-5 [h^-1]

### Oczekiwany wynik
A0 ≤ 0.435 * 10^-5 [h^-1]

---

## Przykład 2: Ustalanie wartości oczekiwanej czasu poprawnej pracy E(T0)

### Opis
Projektowane urządzenie ma być niezawodnościowo podobne do innego urządzenia, dla którego uzyskano E*(T) = 900 [h].

### Dane wejściowe
- Liczba grup elementów: 3
- Współczynniki Kmj:
  - Ekspert 1: 1.1
  - Ekspert 2: 1.2
  - Ekspert 3: 1.2
  - Ekspert 4: 1.3

### Obliczenia
1. Oblicz Km:
   Km = (1/4) * (1.1 + 1.2 + 1.2 + 1.3) = 1.2
2. Oblicz Ke na podstawie Kej:
   Ke ≈ 3.673
3. Oblicz E(T0):
   E(T0) ≥ 900 * 1.2 * 3.7 ≈ 4000 [h]

### Oczekiwany wynik
E(T0) ≥ 4000 [h]

---

## Przykład 3: Ustalanie dopuszczalnej wartości intensywności uszkodzeń λd dla układu scalonego

### Opis
Układ scalony składa się z 1000 bramek, 500 połączeń metalicznych i 16 połączeń termokompresyjnych.

### Dane wejściowe
- Intensywność uszkodzeń:
  - Elementy tranzystorowe: 0.3 * 10^-8 [h^-1]
  - Metalizacja: 0.1 * 10^-8 [h^-1]
  - Połączenia termokompresyjne: 0.1 * 10^-8 [h^-1]
  - Korpus: 1 * 10^-8 [h^-1]

### Obliczenia
1. Oblicz łączną intensywność uszkodzeń:
   Σ λej = [1000*0.3 + 500*0.1 + 16*0.1 + 1*1] * 10^-8 [h^-1]
2. Przyjmij k = 6, α = 1/k ≈ 0.17
3. Oblicz λd:
   λd = 0.17 * Σ λej

### Oczekiwany wynik
λd ≤ 60 * 10^-8 [h^-1]