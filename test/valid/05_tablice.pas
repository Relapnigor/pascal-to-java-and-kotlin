program Tablice;

const
  N = 10;
  ROZMIAR = 5;

var
  tab          : array[0..10] of integer;
  macierz_a    : array[0..4] of real;
  znaki        : array[0..5] of char;
  tekst        : array[0..9] of string;
  i, j         : integer;
  suma, maks   : integer;
  tmp          : integer;

function SzukajMax(n : integer) : integer;
var
  maks : integer;
  i    : integer;
begin
  maks := tab[1];
  for i := 2 to n do
    if tab[i] > maks then
      maks := tab[i];
  return maks;
end;

procedure BubbleSort(n : integer);
var
  i, j  : integer;
  tmp   : integer;
  zmian : boolean;
begin
  for i := 1 to n - 1 do
  begin
    zmian := false;
    for j := 1 to n - i do
    begin
      if tab[j] > tab[j + 1] then
      begin
        tmp := tab[j];
        tab[j] := tab[j + 1];
        tab[j + 1] := tmp;
        zmian := true;
      end;
    end;
    if not zmian then
      break;
  end;
end;

begin
  { Wypelnianie tablicy }
  for i := 1 to 10 do
    tab[i] := i * 2;

  { Odczyt z tablicy }
  suma := 0;
  for i := 1 to 10 do
    suma := suma + tab[i];

  { Modyfikacja elementow }
  tab[1] := 99;
  tab[10] := tab[1] + tab[2];

  { Dostep przez wyrazenie indeksowe }
  j := 3;
  tab[j] := tab[j - 1] + tab[j + 1];

  { Tablica real }
  for i := 0 to 4 do
    macierz_a[i] := i * 1.5;

  macierz_a[2] := macierz_a[0] + macierz_a[1];

  { Zagniezdzony dostep - symulacja macierzy przez indeks }
  for i := 1 to 10 do
  begin
    if tab[i] > 10 then
      tab[i] := tab[i] mod 10;
  end;

  { Wywolanie funkcji i procedur z tablicami }
  maks := SzukajMax(10);
  BubbleSort(10);

  { Uzycie tablicy w wyrazeniach }
  suma := tab[1] + tab[2] + tab[N];
  tmp := tab[suma mod 10 + 1];

  { Przypisania zlozone na elementach tablicy }
  tab[1] += 5;
  tab[2] -= 1;
  tab[3] *= 2;

  { Inkrementacja elementow tablicy }
  tab[1]++;
  tab[2]--;
end.
