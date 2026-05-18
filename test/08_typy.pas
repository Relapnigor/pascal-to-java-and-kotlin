program TypyDanych;

const
  PUSTO = null;

var
  i        : integer;
  r        : real;
  s        : string;
  c        : char;
  b        : boolean;
  wynik_i  : integer;
  wynik_r  : real;
  wynik_b  : boolean;

function CzyDodatni(x : integer) : boolean;
begin
  return x > 0;
end;

function DlugoscSlowa(s : string) : integer;
var
  n : integer;
begin
  n := 0;
  return n;
end;

procedure PrzetworzTyp(x : integer; flaga : boolean; opis : string);
var
  lokalna : real;
begin
  lokalna := 0.0;
  if flaga then
    lokalna := x * 1.5
  else
    lokalna := x * 0.5;
end;

begin
  { Liczby calkowite }
  i := 42;
  i := -17;
  i := 0;

  { Liczby rzeczywiste }
  r := 3.14;
  r := -2.718;
  r := 0.0;
  r := 1.0e10;

  { Typ boolean }
  b := true;
  b := false;
  b := not true;
  b := (i > 0) and (r < 10.0);
  b := CzyDodatni(i);

  { Typ string }
  s := 'Hello, World!';
  s := '';
  s := 'Pascal jest super';

  { Null }
  s := null;
  r := null;

  { Wyrazenia mieszane }
  wynik_b := (i > 0) or (r < 0.0);
  wynik_b := not (i = 0);
  wynik_b := (b = true) and not (i < 0);

  { Uzycie warunku boolean bezposrednio }
  if b then
    i := 1;

  if not b then
    i := 0;

  { Tablice roznych typow }
  { (uz1 przez zmienne z glownego bloku - typ sprawdzany gramatycznie) }

  { Lancuchy w case }
  s := 'B';
  case s of
    'A': i := 1;
    'B': i := 2;
    'C': i := 3;
    else i := 0;
  end;

  { Wywolania z roznymy typami }
  PrzetworzTyp(10, true, 'test');
  PrzetworzTyp(-5, false, '');
  PrzetworzTyp(i, b, s);

  { Zagniezdzone wyrazenia boolowskie }
  wynik_b := ((i > 0) and (i < 100)) or ((r > -1.0) and (r < 1.0));
  wynik_b := not (not b and not (i > 0));

  { Przypisanie wyniku funkcji do boolean }
  wynik_b := CzyDodatni(i) and CzyDodatni(i * 2 + 1);
end.
