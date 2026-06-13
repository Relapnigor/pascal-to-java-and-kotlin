program BubbleSort;
var
  tab : array[1..11] of integer;
  i, j, n, tmp : integer;
begin
  n := 10;
  tab[1] := 64;
  tab[2] := 34;
  tab[3] := 25;
  tab[4] := 12;
  tab[5] := 22;
  tab[6] := 11;
  tab[7] := 90;
  tab[8] := 5;
  tab[9] := 77;
  tab[10] := 1;

  WriteLn('Tablica przed sortowaniem:');
  for i := 1 to n do
    WriteLn(tab[i]);

  for i := 1 to n - 1 do
  begin
    for j := 1 to n - i do
    begin
      if tab[j] > tab[j + 1] then
      begin
        tmp := tab[j];
        tab[j] := tab[j + 1];
        tab[j + 1] := tmp;
      end;
    end;
  end;

  WriteLn('Tablica po sortowaniu:');
  for i := 1 to n do
    WriteLn(tab[i]);
end.