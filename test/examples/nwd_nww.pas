program NwdNww;
var
  a, b, wynikNWD, wynikNWW : integer;

function NWD(a : integer; b : integer) : integer;
var
  tmp : integer;
begin
  while b != 0 do
  begin
    tmp := b;
    b := a mod b;
    a := tmp;
  end;
  return a;
end;

begin
  a := 48;
  b := 18;

  WriteLn('Liczba A:');
  WriteLn(a);
  WriteLn('Liczba B:');
  WriteLn(b);

  wynikNWD := NWD(a, b);
  WriteLn('NWD:');
  WriteLn(wynikNWD);

  wynikNWW := (a * b) div wynikNWD;
  WriteLn('NWW:');
  WriteLn(wynikNWW);
end.