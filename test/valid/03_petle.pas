program Petle;

var
  i, j, n  : integer;
  suma      : integer;
  iloczyn   : integer;

begin
  n := 10;

  { Petla while }
  i := 1;
  suma := 0;
  while i <= n do
  begin
    suma := suma + i;
    i++;
  end;

  { Petla while z break }
  i := 0;
  while true do
  begin
    i++;
    if i >= 5 then
      break;
  end;

  { Petla while z continue }
  suma := 0;
  i := 0;
  while i < n do
  begin
    i++;
    if i mod 2 = 0 then
      continue;
    suma := suma + i;
  end;

  { Petla for to }
  suma := 0;
  for i := 1 to n do
    suma := suma + i;

  { Petla for downto }
  suma := 0;
  for i := n downto 1 do
    suma := suma + i;

  { Petla for z blokiem }
  iloczyn := 1;
  for i := 1 to 5 do
  begin
    iloczyn := iloczyn * i;
    suma := suma + iloczyn;
  end;

  { Zagniezdzzone petle for }
  suma := 0;
  for i := 1 to n do
    for j := 1 to n do
      suma := suma + i * j;

  { Zagniezdzzone petle z break }
  for i := 1 to n do
  begin
    for j := 1 to n do
    begin
      if j > i then
        break;
      suma := suma + 1;
    end;
  end;

  { Petla repeat-until }
  i := 1;
  suma := 0;
  repeat
    suma := suma + i;
    i++;
  until i > n;

  { Repeat z warunkiem zlozonym }
  i := 0;
  j := 100;
  repeat
    i++;
    j--;
  until (i >= 10) or (j <= 90);

  { Repeat z wieloma instrukcjami }
  i := 1;
  iloczyn := 1;
  repeat
    iloczyn := iloczyn * i;
    i++;
    if iloczyn > 1000 then
      break;
  until i > 20;
end.
