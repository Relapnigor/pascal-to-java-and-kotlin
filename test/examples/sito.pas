program SitoEratostenesa;
var
  sito : array[1..100] of integer;
  i, j, n : integer;

begin
  n := 50;

  for i := 1 to n do
    sito[i] := 1;

  sito[1] := 0;

  i := 2;
  while i * i <= n do
  begin
    if sito[i] = 1 then
    begin
      j := i * i;
      while j <= n do
      begin
        sito[j] := 0;
        j := j + i;
      end;
    end;
    i++;
  end;

  WriteLn('Liczby pierwsze do 50:');
  for i := 2 to n do
    if sito[i] = 1 then
      WriteLn(i);
end.