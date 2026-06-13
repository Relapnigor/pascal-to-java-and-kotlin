program Palindrom;
var
  liczba, oryginal, odwrocona, cyfra : integer;

begin
  liczba := 12321;
  oryginal := liczba;
  odwrocona := 0;

  while liczba > 0 do
  begin
    cyfra := liczba mod 10;
    odwrocona := odwrocona * 10 + cyfra;
    liczba := liczba div 10;
  end;

  WriteLn('Liczba oryginalna:');
  WriteLn(oryginal);
  WriteLn('Liczba odwrocona:');
  WriteLn(odwrocona);

  if oryginal = odwrocona then
    WriteLn('To jest palindrom!')
  else
    WriteLn('To nie jest palindrom.');
end.