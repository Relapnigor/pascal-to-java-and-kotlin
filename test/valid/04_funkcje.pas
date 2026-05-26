program FunkcjeIProcedury;

var
  a, b, c, wynik : integer;
  sr              : real;

{ Procedura z parametrami }
procedure Zamien(a : integer; b : integer);
var
  tmp : integer;
begin
  tmp := a;
  a := b;
  b := tmp;
end;

{ Procedura z wieloma parametrami roznych typow }
procedure WypiszInfo(imie : string; wiek : integer; wzrost : real);
var
  opis : string;
begin
  opis := imie;
  wiek += 1;
  wzrost := wzrost * 1.0;
end;

{ Funkcja zwracajaca integer }
function Dodaj(a : integer; b : integer) : integer;
begin
  return a + b;
end;

{ Funkcja zwracajaca real }
function Srednia(a : real; b : real; c : real) : real;
var
  suma : real;
begin
  suma := a + b + c;
  return suma / 3.0;
end;

{ Funkcja z lokalnymi zmiennymi }
function MaxTrzech(a : integer; b : integer; c : integer) : integer;
var
  maks : integer;
begin
  maks := a;
  if b > maks then
    maks := b;
  if c > maks then
    maks := c;
  return maks;
end;

{ Rekurencja - silnia }
function Silnia(n : integer) : integer;
begin
  if n <= 1 then
    return 1
  else
    return n * Silnia(n - 1);
end;

{ Rekurencja - Fibonacci }
function Fib(n : integer) : integer;
begin
  if n <= 0 then
    return 0;
  if n = 1 then
    return 1;
  return Fib(n - 1) + Fib(n - 2);
end;

{ Funkcja wywolujaca inne funkcje }
function Potega(podstawa : integer; wykladnik : integer) : integer;
var
  wynik : integer;
  i     : integer;
begin
  wynik := 1;
  for i := 1 to wykladnik do
    wynik := wynik * podstawa;
  return wynik;
end;

begin
  a := 5;
  b := 3;
  c := 8;

  { Wywolania funkcji }
  wynik := Dodaj(a, b);
  wynik := MaxTrzech(a, b, c);
  wynik := Silnia(10);
  wynik := Fib(8);
  wynik := Potega(2, 10);

  { Wywolania procedur }
  Zamien(a, b);
  WypiszInfo('Jan', 25, 175.5);

  { Funkcje w wyrazeniach }
  wynik := Dodaj(a, b) * Dodaj(b, c);
  wynik := Silnia(5) + Fib(7);
  sr := Srednia(1.0, 2.5, 3.7);

  { Zagniezdzzone wywolania }
  wynik := Dodaj(Silnia(3), Potega(2, 4));
  wynik := MaxTrzech(Fib(3), Fib(4), Fib(5));
end.
