program Warunki;

var
  a, b, c : integer;
  x       : real;
  flaga   : boolean;

begin
  a := 10;
  b := 20;
  c := 10;

  { Proste if }
  if a > 0 then
    b := 1;

  { if-else }
  if a > b then
    c := a
  else
    c := b;

  { Zagniezdzony if-else }
  if a > 100 then
    c := 3
  else if a > 50 then
    c := 2
  else if a > 0 then
    c := 1
  else
    c := 0;

  { Warunki z operatorami logicznymi }
  if (a > 0) and (b > 0) then
    c := a + b;

  if (a > 100) or (b > 100) then
    c := 0;

  if not (a = b) then
    c := -1;

  { Zlozony warunek logiczny }
  if ((a > 0) and (b > 0)) or (c = 0) then
    a := 1
  else
    a := 0;

  { Wszystkie operatory porownania }
  if a > b  then c := 1;
  if a < b  then c := 2;
  if a = b  then c := 3;
  if a >= b then c := 4;
  if a <= b then c := 5;
  if a != b then c := 6;

  { if z blokiem begin-end }
  if a > 0 then
  begin
    b := a * 2;
    c := b + 1;
  end
  else
  begin
    b := 0;
    c := 0;
  end;

  { Zagniezdzony if z blokami }
  if a > 0 then
  begin
    if b > 0 then
    begin
      c := a + b;
      a := c * 2;
    end
    else
      c := a;
  end;
end.
