program Test;

const
    A = 10;
    B = 5;

var
  x, y, z, ocena: Integer;

function Sub(a,b: Integer): Integer;
begin
    Sub := a - b;
end;

function Add(p, q: Integer): Integer;
begin
    Add := p + q;
end;

function Max(p, q: Integer): Integer;
begin
  if p > q then
    Max := p
  else
    Max := q;
end;

begin
    WriteLn('Hello world');
    x := Add(5, 3);
    y := Sub(10,3);
    WriteLn(x);
    WriteLn(y);
    if x > y then
    begin
        WriteLn('yes');
        Writeln('yes');
        x -= 1;
        if x > y then
            WriteLn('elo');
    end
    else
    begin
        WriteLn('no');
        Writeln('no');
        x += 1;
        if x > y then
            WriteLn('yo')
        else
            WriteLn('yo');

    end;

    ocena := x;
    if ocena > 4 then
      writeln('Bardzo dobrze')
    else if ocena > 2 then
      writeln('Przeszedles')
    else
      writeln('Oblales');
end.
