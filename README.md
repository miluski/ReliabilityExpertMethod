# Prognozowanie Niezawodności - Metoda Ekspertów

System do prognozowania wskaźników niezawodności systemów technicznych metodą ekspertów z interfejsem graficznym (PyQt5).

## 📋 Opis

Program umożliwia obliczanie wskaźników niezawodności dla projektowanych urządzeń technicznych na podstawie opinii ekspertów (mechaników i elektroników). System jest w pełni uogólniony - działa dla dowolnej liczby ekspertów, grup elementów i modułów.

### Główne funkcje:

- Obliczanie współczynnika konstrukcyjnego **αk** (na podstawie ocen mechaników)
- Obliczanie współczynnika elementowego **αe** (na podstawie ocen elektroników)
- Obliczanie współczynnika eksploatacyjnego **Ke**
- Wyznaczanie **A0** (średni strumień uszkodzeń)
- Wyznaczanie **E(T0)** (oczekiwany czas poprawnej pracy)
- Wyznaczanie **λdi** (intensywność uszkodzeń nowych elementów)
- Obliczanie wag modułów metodą ankietową
- Interfejs graficzny (PyQt5) z zakładkami
- Walidacja danych wejściowych
- Wizualizacja wyników

## 🔧 Wymagania

- **Python 3.8+**
- **System operacyjny**: Windows, macOS, Linux

### Biblioteki Python:

```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
plotly>=5.0.0
PyQt5>=5.15.0
openpyxl>=3.0.0
```

## 📥 Instalacja

1. Zainstaluj zależności: `pip install -r requirements.txt`
2. Uruchom program: `python src/main.py`

## 🎯 Użycie programu

### Interfejs graficzny (3 zakładki):

1. **Konfiguracja**: Wybierz tryb obliczeń (A0/E(T0)/λdi), liczba ekspertów, dane prognostyczne
2. **Dane Ekspertów**: Wprowadź wartości Kmj dla mechaników (1.0-2.0) i tabele Ng/N, Kg dla elektroników
3. **Wyniki**: Zobacz obliczone współczynniki αk, αe, Ke i wynik końcowy

### Przykładowe wartości testowe:

**Konfiguracja:**

- Tryb: Obliczanie A0, Mechanicy: 3, Elektronicy: 5, Ā: `1.1e-5`

**Mechanicy (Kmj):**

- Mechanik 1: 1.2, Mechanik 2: 1.2, Mechanik 3: 1.2

**Elektronicy (tabele Ng/N, Kg):**

- Elektronik 1: [0.50,10], [0.30,3], [0.15,4], [0.05,2]
- Elektronik 2: [0.45,9], [0.25,4], [0.20,5], [0.10,3]

**Oczekiwane wyniki:**

- Km = 1.2, αk ≈ 0.83, αe ≈ 0.46, A0 ≤ 4.35×10⁻⁶

## 🔨 Budowanie wersji wykonywalnej

### Windows:

```bash
build_windows.bat
```

### macOS/Linux:

```bash
chmod +x build_macos_linux.sh
./build_macos_linux.sh
```

**Wymagania:** `pip install pyinstaller`

**Wyjście:**

- Windows: `dist/ReliabilityExpert.exe`
- macOS: `dist/ReliabilityExpert` (uruchom: `./dist/ReliabilityExpert`)
- Linux: `dist/ReliabilityExpert` (uruchom: `./dist/ReliabilityExpert`)

**Uwagi:**

- macOS: Używa `--collect-all=PyQt5` dla poprawnego działania
- Jeśli problemy z budowaniem: sprawdź `pip install PyQt5 pyinstaller`

## 🧪 Testowanie

```bash
cd tests && python test_calculations.py
```

## 📐 Wzory matematyczne

- **αk** = 1/Km, gdzie Km = (1/J) × Σ Kmj
- **αe** = (1/J) × Σ αej, αej = Σ (Ng/N × 1/Kg)
- **Ke** = (1/J) × Σ Kej, Kej = Σ (Ng/N × Kgj)
- **A0** ≤ Ā × αe × αk
- **E(T0)** ≥ E\*(T) × Km × Ke
- **λdi** = λp × αi, gdzie αi = 1/ki

## 🏗️ Struktura projektu

```
src/
├── main.py
├── calculations/
├── gui/
├── utils/
└── data/
tests/
```

## Metoda ekspertów

Heurystyczna technika prognozowania używana gdy brak danych statystycznych o awaryjności.

### Grupy elementów:

1. Dyskretne (rezystory, kondensatory, tranzystory)
2. Scalone (mikrokontrolery, pamięci)
3. Elektryczne (przekaźniki, złącza)
4. Mechaniczne (obudowy, mechanizmy)

## Przykłady obliczeń

### Przykład 1: Woltomierz cyfrowy (tryb A0)

- **Mechanicy**: J=3, Kmj=[1.2, 1.2, 1.2] → Km=1.2 → αk≈0.83
- **Elektronicy**: J=5 ekspertów z danymi Ng/N i Kg → αe≈0.46
- **Wynik**: A0 ≤ Ā × αe × αk = 1.1×10⁻⁵ × 0.46 × 0.83 ≈ 4.35×10⁻⁶ h⁻¹

### Przykład 2: Urządzenie (tryb E(T0))

- **Mechanicy**: J=4, Kmj=[1.1, 1.2, 1.2, 1.3] → Km=1.2
- **Elektronicy**: J=4 ekspertów → Ke≈3.67
- **Wynik**: E(T0) ≥ E\*(T) × Km × Ke = 900 × 1.2 × 3.67 ≈ 4000h
