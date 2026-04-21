# 🔄 Konwerter Pascala → Java i Kotlin

## 👥 Autorzy

| Imię i nazwisko | E-mail                      |
|-----------------|-----------------------------|
| Maciej Dziobek  | mdziobek@student.agh.edu.pl |
| Robert Filas    | rfilas@student.agh.edu.pl   |

---

## 📋 Opis projektu

Program konwertuje kod źródłowy w języku **Pascal** (z wybranymi rozszerzeniami) na równoważny kod w językach **Java** oraz **Kotlin**.

Planowane jest utworzenie interfejsu graficznego umożliwiającego:
- wybór pliku wejściowego `.pas` do konwersji,
- podgląd wygenerowanych plików wynikowych,
- pobranie plików `.java` oraz `.kt`.

---

## ⚙️ Specyfikacja techniczna

| Parametr            | Wartość                                      |
|---------------------|----------------------------------------------|
| Rodzaj translatora  | Kompilator                                   |
| Język implementacji | Python                                       |
| Skaner / parser     | [Lark](https://github.com/lark-parser/lark)  |
| Dane wejściowe      | Kod źródłowy Pascal (`.pas`)                 |
| Dane wyjściowe      | Kod źródłowy Java (`.java`) i Kotlin (`.kt`) |

---

## 📘 Tokeny gramatyki

---

Cała gramatyka znajduje się w pliku [grammar.lark](https://github.com/Relapnigor/pascal-to-java-and-kotlin/blob/main/grammar/grammar.lark)

---

### Identyfikatory i literały

| Token    | Wzorzec                                                                 | Opis |
|----------|--------------------------------------------------------------------------|------|
| `NAME`   | `[A-Za-z_][A-Za-z0-9_]*`                                                | Identyfikator — nazwa zmiennej, funkcji, procedury lub typu |
| `NUMBER` | liczby całkowite i rzeczywiste (float, e-notation)                      | Literał liczbowy (ogólny) |
| `INT`    | `[0-9]+`                                                                | Literał liczby całkowitej (np. indeksy tablic) |
| `STRING` | `'[^']*'`                                                               | Literał tekstowy |
| `TYPE`   | `integer | real | string | char | boolean` (case-insensitive)           | Typ danych |
| `BOOL`   | `true | false` (case-insensitive)                                      | Literał logiczny |
| `NULL`   | `null`                                                                  | Wartość pustego wskaźnika |

---

### Komentarze i białe znaki (ignorowane)

| Token      | Wzorzec        | Opis |
|------------|----------------|------|
| `COMMENT1` | `{...}`        | Komentarz blokowy |
| `COMMENT2` | `(* ... *)`    | Komentarz blokowy (multi-line) |
| `WS`       | `[ \t\r\n]+`   | Białe znaki |

---

### Operatory arytmetyczne

| Token         | Symbol | Opis |
|---------------|--------|------|
| `PLUS`        | `+`    | Dodawanie |
| `MINUS`       | `-`    | Odejmowanie |
| `STAR`        | `*`    | Mnożenie |
| `SLASH`       | `/`    | Dzielenie rzeczywiste |
| `DIV`         | `div`  | Dzielenie całkowite |
| `MOD`         | `mod`  | Reszta z dzielenia |
| `POW`         | `^`    | Potęgowanie |

---

### Operatory przypisania (rozszerzone)

| Token          | Symbol | Opis |
|----------------|--------|------|
| `ASSIGN`       | `:=`   | Przypisanie |
| `PLUS_ASSIGN`  | `+=`   | Dodaj i przypisz |
| `MINUS_ASSIGN` | `-=`   | Odejmij i przypisz |
| `MUL_ASSIGN`   | `*=`   | Mnoż i przypisz |
| `DIV_ASSIGN`   | `/=`   | Dziel i przypisz |

---

### Operatory porównania

| Token       | Symbol | Opis |
|-------------|--------|------|
| `EQUAL`     | `=`    | Równość |
| `NE`        | `!=`   | Nierówność |
| `MORETHAN`  | `>`    | Większy niż |
| `LESSTHAN`  | `<`    | Mniejszy niż |
| `GE`        | `>=`   | Większy lub równy |
| `LE`        | `<=`   | Mniejszy lub równy |

---

### Operatory logiczne

| Token | Symbol | Opis |
|------|--------|------|
| `AND` | `and`  | AND logiczne |
| `OR`  | `or`   | OR logiczne |
| `NOT` | `not`  | NOT logiczne |

---

### Operatory sterujące (rozszerzenie)

| Token       | Symbol     | Opis |
|-------------|------------|------|
| `BREAK`     | `break`    | Przerwanie pętli |
| `CONTINUE`  | `continue` | Pominięcie iteracji |

---

### Słowa kluczowe

| Token       | Symbol      | Opis |
|-------------|-------------|------|
| `PROGRAM`   | `program`   | Program główny |
| `VAR`       | `var`       | Sekcja zmiennych |
| `CONST`     | `const`     | Sekcja stałych |
| `FUNCTION`  | `function`  | Funkcja |
| `PROCEDURE` | `procedure` | Procedura |
| `BEGIN`     | `begin`     | Blok kodu |
| `END`       | `end`       | Koniec bloku |
| `IF`        | `if`        | Warunek |
| `THEN`      | `then`      | Gałąź if |
| `ELSE`      | `else`      | Alternatywa |
| `WHILE`     | `while`     | Pętla while |
| `FOR`       | `for`       | Pętla for |
| `TO`        | `to`        | rosnąco |
| `DOWNTO`    | `downto`    | malejąco |
| `REPEAT`    | `repeat`    | repeat-until |
| `UNTIL`     | `until`     | warunek końca |
| `RETURN`    | `return`    | zwrot wartości |
| `CASE`      | `case`      | switch |
| `OF`        | `of`        | case separator |
| `ARRAY`     | `array`     | tablice |

---

### Interpunkcja

| Token       | Symbol | Opis |
|-------------|--------|------|
| `SEMICOLON` | `;`    | separator instrukcji |
| `COLON`     | `:`    | typ / etykieta |
| `DOT`       | `.`    | koniec programu |
| `COMMA`     | `,`    | lista argumentów |
| `LPAR`      | `(`    | nawias otwierający |
| `RPAR`      | `)`    | nawias zamykający |
| `LSQB`      | `[`    | tablice |
| `RSQB`      | `]`    | tablice |
| `RANGE`     | `..`   | zakres |