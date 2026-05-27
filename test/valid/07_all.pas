program Kompleksowy;

{ Program testujacy wiele funkcjonalnosci naraz:
  stale, zmienne, tablice, funkcje, procedury,
  petle, warunki, case, rekurencja }

const
  MAX_N    = 20;
  SENTINEL = -1;
  PI       = 3.14159265;

var
  dane     : array[1..20] of integer;
  n        : integer;
  i        : integer;
  wynik    : integer;

{ ===== Funkcje pomocnicze ===== }

function Abs(x : integer) : integer;
begin
  if x < 0 then
    return -x;
  return x;
end;

function Min(a : integer; b : integer) : integer;
begin
  if a < b then
    return a;
  return b;
end;

function Max(a : integer; b : integer) : integer;
begin
  if a > b then
    return a;
  return b;
end;

function CzyPierwsza(n : integer) : boolean;
var
  i : integer;
begin
  if n < 2 then
    return false;
  if n = 2 then
    return true;
  if n mod 2 = 0 then
    return false;
  i := 3;
  while i * i <= n do
  begin
    if n mod i = 0 then
      return false;
    i += 2;
  end;
  return true;
end;

function NWD(a : integer; b : integer) : integer;
begin
  while b != 0 do
  begin
    a := a mod b;
    wynik := a;
    a := b;
    b := wynik;
  end;
  return a;
end;

function NWW(a : integer; b : integer) : integer;
begin
  return (a * b) div NWD(a, b);
end;

function Silnia(n : integer) : integer;
begin
  if n <= 1 then
    return 1;
  return n * Silnia(n - 1);
end;

{ ===== Procedury operujace na tablicy ===== }

procedure WypelnijLosowo(n : integer);
var
  i : integer;
begin
  for i := 1 to n do
    dane[i] := (i * 17 + 13) mod 100;
end;

procedure SortujWstawkowe(n : integer);
var
  i, j  : integer;
  klucz : integer;
begin
  for i := 2 to n do
  begin
    klucz := dane[i];
    j := i - 1;
    while (j >= 1) and (dane[j] > klucz) do
    begin
      dane[j + 1] := dane[j];
      j--;
    end;
    dane[j + 1] := klucz;
  end;
end;

function SumaZakresu(lewy : integer; prawy : integer) : integer;
var
  i    : integer;
  suma : integer;
begin
  suma := 0;
  for i := lewy to prawy do
    suma := suma + dane[i];
  return suma;
end;

function LiczPierwsze(n : integer) : integer;
var
  i    : integer;
  ile  : integer;
begin
  ile := 0;
  for i := 1 to n do
    if CzyPierwsza(dane[i]) then
      ile++;
  return ile;
end;

{ ===== Glowny program ===== }

begin
  n := 15;
  WriteLn('=== Program Kompleksowy ===');

  { Wypelnij i posortuj tablice }
  WypelnijLosowo(n);
  WriteLn('Tablica wypelniona.');
  SortujWstawkowe(n);
  WriteLn('Tablica posortowana.');

  { Wypisz posortowana tablice }
  WriteLn('Elementy tablicy:');
  for i := 1 to n do
    WriteLn(dane[i]);

  { Statystyki }
  wynik := SumaZakresu(1, n);
  WriteLn('Suma elementow:');
  WriteLn(wynik);

  wynik := LiczPierwsze(n);
  WriteLn('Liczba pierwszych w tablicy:');
  WriteLn(wynik);

  { Test funkcji matematycznych }
  wynik := NWD(48, 18);
  WriteLn('NWD(48, 18):');
  WriteLn(wynik);

  wynik := NWW(4, 6);
  WriteLn('NWW(4, 6):');
  WriteLn(wynik);

  wynik := Silnia(7);
  WriteLn('Silnia(7):');
  WriteLn(wynik);

  { Test CzyPierwsza dla zakresu 2..50 }
  wynik := 0;
  for i := 2 to 50 do
  begin
    if CzyPierwsza(i) then
      wynik++;
  end;
  WriteLn('Liczba pierwszych w zakresie 2..50:');
  WriteLn(wynik);

  { Operacje na tablicy z case }
  for i := 1 to n do
  begin
    case dane[i] mod 3 of
      0: dane[i] := dane[i] + 1;
      1: dane[i] := dane[i] * 2;
      2: dane[i] := dane[i] - 1;
    end;
  end;
  WriteLn('Tablica po operacjach case:');
  for i := 1 to n do
    WriteLn(dane[i]);

  { Zlozony warunek z petla }
  i := 1;
  wynik := 0;
  repeat
    if (dane[i] > 10) and (dane[i] < 90) then
    begin
      if CzyPierwsza(dane[i]) then
        wynik += dane[i]
      else
        wynik += 1;
    end;
    i++;
  until (i > n) or (wynik > 500);
  WriteLn('Wynik po petli repeat:');
  WriteLn(wynik);

  { Uzycie Min i Max }
  wynik := dane[1];
  for i := 2 to n do
    wynik := Max(wynik, dane[i]);
  WriteLn('Maksimum tablicy:');
  WriteLn(wynik);

  { Finalne obliczenie }
  wynik := NWD(Silnia(4), Silnia(5)) + LiczPierwsze(n);
  wynik := Min(wynik, MAX_N);
  WriteLn('Wynik finalny (max MAX_N):');
  WriteLn(wynik);

  WriteLn('=== Koniec ===');
end.