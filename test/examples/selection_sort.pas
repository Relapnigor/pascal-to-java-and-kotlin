program SelectionSort;
var
  tab : array[1..9] of integer;
  i, j, n, minIdx, tmp : integer;
begin
  n := 8;
  tab[1] := 29;
  tab[2] := 10;
  tab[3] := 14;
  tab[4] := 37;
  tab[5] := 13;
  tab[6] := 4;
  tab[7] := 99;
  tab[8] := 2;

  WriteLn('Przed sortowaniem:');
  for i := 1 to n do
    WriteLn(tab[i]);

  for i := 1 to n - 1 do
  begin
    minIdx := i;
    for j := i + 1 to n do
      if tab[j] < tab[minIdx] then
        minIdx := j;

    if minIdx != i then
    begin
      tmp := tab[i];
      tab[i] := tab[minIdx];
      tab[minIdx] := tmp;
    end;
  end;

  WriteLn('Po sortowaniu:');
  for i := 1 to n do
    WriteLn(tab[i]);
end.