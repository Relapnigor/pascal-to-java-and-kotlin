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

## 🔤 Tokeny gramatyki
Cała gramatyka znajduje się w katalogu [grammar](https://github.com/Relapnigor/pascal-to-java-and-kotlin/tree/main/grammar).

### Identyfikatory i literały

| Token    | Wzorzec                                | Opis                                                  |
|----------|----------------------------------------|-------------------------------------------------------|
| `NAME`   | `[A-Za-z_][A-Za-z0-9_]*`               | Identyfikator — nazwa zmiennej, funkcji lub procedury |
| `NUMBER` | `[0-9]+(\.[0-9]+)?(e[+-]?[0-9]+)?`     | Literał liczbowy — całkowity lub rzeczywisty          |
| `STRING` | `'[^']*'`                              | Literał tekstowy w apostrofach                        |
| `TYPE`   | `integer\|real\|string\|char\|boolean` | Nazwa typu danych                                     |

### Komentarze i białe znaki (ignorowane)

| Token      | Wzorzec      | Opis                                                    |
|------------|--------------|---------------------------------------------------------|
| `COMMENT1` | `{...}`      | Komentarz w nawiasach klamrowych                        |
| `COMMENT2` | `(*...*)`    | Komentarz w nawiasach z gwiazdką, może być wieloliniowy |
| `WS`       | `[ \t\r\n]+` | Białe znaki — spacje, tabulatory, nowe linie            |

### Operatory arytmetyczne

| Token   | Symbol | Opis                                     |
|---------|--------|------------------------------------------|
| `PLUS`  | `+`    | Dodawanie                                |
| `MINUS` | `-`    | Odejmowanie lub negacja jednoargumentowa |
| `STAR`  | `*`    | Mnożenie                                 |
| `SLASH` | `/`    | Dzielenie rzeczywiste                    |
| `DIV`   | `div`  | Dzielenie całkowite                      |
| `MOD`   | `mod`  | Reszta z dzielenia                       |

### Operatory porównania

| Token      | Symbol | Opis               |
|------------|--------|--------------------|
| `EQUAL`    | `=`    | Równość            |
| `NE`       | `!=`   | Nierówność         |
| `MORETHAN` | `>`    | Większy niż        |
| `LESSTHAN` | `<`    | Mniejszy niż       |
| `GE`       | `>=`   | Większy lub równy  |
| `LE`       | `<=`   | Mniejszy lub równy |

### Operatory logiczne

| Token | Symbol | Opis                 |
|-------|--------|----------------------|
| `AND` | `and`  | Koniunkcja logiczna  |
| `OR`  | `or`   | Alternatywa logiczna |
| `NOT` | `not`  | Negacja logiczna     |

### Operator przypisania

| Token    | Symbol | Opis                             |
|----------|--------|----------------------------------|
| `ASSIGN` | `:=`   | Przypisanie wartości do zmiennej |

### Słowa kluczowe

| Token       | Symbol      | Opis                                   |
|-------------|-------------|----------------------------------------|
| `PROGRAM`   | `program`   | Początek programu                      |
| `VAR`       | `var`       | Sekcja deklaracji zmiennych            |
| `FUNCTION`  | `function`  | Deklaracja funkcji zwracającej wartość |
| `PROCEDURE` | `procedure` | Deklaracja procedury                   |
| `BEGIN`     | `begin`     | Początek bloku instrukcji              |
| `END`       | `end`       | Koniec bloku instrukcji                |
| `IF`        | `if`        | Instrukcja warunkowa                   |
| `THEN`      | `then`      | Gałąź warunku `if`                     |
| `ELSE`      | `else`      | Gałąź alternatywna warunku `if`        |
| `WHILE`     | `while`     | Pętla z warunkiem na początku          |
| `DO`        | `do`        | Ciało pętli `while` lub `for`          |
| `FOR`       | `for`       | Pętla licząca                          |
| `TO`        | `to`        | Kierunek pętli `for` — rosnąco         |
| `DOWNTO`    | `downto`    | Kierunek pętli `for` — malejąco        |
| `REPEAT`    | `repeat`    | Początek pętli z warunkiem na końcu    |
| `UNTIL`     | `until`     | Warunek zakończenia pętli `repeat`     |
| `RETURN`    | `return`    | Zwrócenie wartości z funkcji           |

### Interpunkcja

| Token       | Symbol | Opis                                |
|-------------|--------|-------------------------------------|
| `SEMICOLON` | `;`    | Separator instrukcji                |
| `COLON`     | `:`    | Separator nazwy i typu w deklaracji |
| `DOT`       | `.`    | Koniec programu                     |
| `COMMA`     | `,`    | Separator elementów listy           |
| `LPAR`      | `(`    | Nawias otwierający                  |
| `RPAR`      | `)`    | Nawias zamykający                   |