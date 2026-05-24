program Arytmetyka;

const
  PI = 3.14159;
  MAX = 100;

var
  a, b, c : integer;
  x, y    : real;
  wynik   : real;

begin
  a := 10;
  b := 3;

  { Podstawowe operacje arytmetyczne }
  c := a + b;
  c := a - b;
  c := a * b;

  { Dzielenie calkowite i modulo }
  c := a div b;
  c := a mod b;

  { Dzielenie zmiennoprzecinkowe }
  x := 10.0;
  y := 3.0;
  wynik := x / y;

  { Potegowanie }
  wynik := x ^ 2;

  { Operacje z uzyciem stalych }
  wynik := PI * x ^ 2;
  c := MAX div 4;

  { Przypisania zlozone }
  a += 5;
  a -= 2;
  a *= 3;
  a /= 2;

  { Inkrementacja i dekrementacja }
  a++;
  b--;
  ++a;
  --b;

  { Wyrazenia zagniezdzzone }
  wynik := (a + b) * (a - b) / (x + y);
  c := ((a + 1) * b) mod MAX;

  { Negacja }
  wynik := -x;
  c := -(a + b);
end.
