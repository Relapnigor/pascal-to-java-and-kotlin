# Projekt konwertera Pascala do Javy oraz Kotlina

## Autorzy:
- Maciej Dziobek: mdziobek@student.agh.edu.pl
- Robert Filas: rfilas@student.agh.edu.pl

## Założenia programu:
Program ma na celu konwersje wybranego kodu w języku Pascal (z pewnymi rozszerzeniami) na kody w językach Java oraz Kotlin.
Planowane jest utworzenie interfejsu graficznego umożliwiającego wybór pliku do konwersji, a następnie wyświetlenie plików wynikowych z możliwością ich pobrania.

### Rodzaj translatora:
Kompilator

### Planowany wynik działania:
Konwerter Pascala do Javy i Kotlina

### Planowany język implementacji:
Python

### Sposób realizacji skanera/parsera:
Lark

### Tokeny gramatyki

#### Identyfikatory i literały

| Token    | Wzorzec                                | Opis                                                  |
|----------|----------------------------------------|-------------------------------------------------------|
| `NAME`   | `[A-Za-z_][A-Za-z0-9_]*`               | Identyfikator — nazwa zmiennej, funkcji lub procedury |
| `NUMBER` | `[0-9]+(\.[0-9]+)?(e[+-]?[0-9]+)?`     | Literał liczbowy — całkowity lub rzeczywisty          |
| `STRING` | `'[^']*'`                              | Literał tekstowy w apostrofach                        |
| `TYPE`   | `integer\|real\|string\|char\|boolean` | Nazwa typu danych                                     |

#### Komentarze i białe znaki (ignorowane)

| Token      | Wzorzec      | Opis                                                    |
|------------|--------------|---------------------------------------------------------|
| `COMMENT1` | `{...}`      | Komentarz w nawiasach klamrowych                        |
| `COMMENT2` | `(*...*)`    | Komentarz w nawiasach z gwiazdką, może być wieloliniowy |
| `WS`       | `[ \t\r\n]+` | Białe znaki — spacje, tabulatory, nowe linie            |

#### Operatory arytmetyczne

| Token   | Symbol | Opis                                     |
|---------|--------|------------------------------------------|
| `PLUS`  | `+`    | Dodawanie                                |
| `MINUS` | `-`    | Odejmowanie lub negacja jednoargumentowa |
| `STAR`  | `*`    | Mnożenie                                 |
| `SLASH` | `/`    | Dzielenie rzeczywiste                    |
| `DIV`   | `div`  | Dzielenie całkowite                      |
| `MOD`   | `mod`  | Reszta z dzielenia                       |

#### Operatory porównania

| Token      | Symbol | Opis               |
|------------|--------|--------------------|
| `EQUAL`    | `=`    | Równość            |
| `NE`       | `!=`   | Nierówność         |
| `MORETHAN` | `>`    | Większy niż        |
| `LESSTHAN` | `<`    | Mniejszy niż       |
| `GE`       | `>=`   | Większy lub równy  |
| `LE`       | `<=`   | Mniejszy lub równy |

#### Operatory logiczne

| Token | Symbol | Opis                 |
|-------|--------|----------------------|
| `AND` | `and`  | Koniunkcja logiczna  |
| `OR`  | `or`   | Alternatywa logiczna |
| `NOT` | `not`  | Negacja logiczna     |

#### Operator przypisania

| Token    | Symbol | Opis                             |
|----------|--------|----------------------------------|
| `ASSIGN` | `:=`   | Przypisanie wartości do zmiennej |

#### Słowa kluczowe

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

#### Interpunkcja

| Token       | Symbol | Opis                                |
|-------------|--------|-------------------------------------|
| `SEMICOLON` | `;`    | Separator instrukcji                |
| `COLON`     | `:`    | Separator nazwy i typu w deklaracji |
| `DOT`       | `.`    | Koniec programu                     |
| `COMMA`     | `,`    | Separator elementów listy           |
| `LPAR`      | `(`    | Nawias otwierający                  |
| `RPAR`      | `)`    | Nawias zamykający                   |
