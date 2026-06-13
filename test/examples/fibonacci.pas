program Fibonacci;
var
  i, n : integer;
  a, b, tmp : integer;

function FibRekurencyjnie(n : integer) : integer;
begin
  if n <= 1 then
    return n;
  return FibRekurencyjnie(n - 1) + FibRekurencyjnie(n - 2);
end;

begin
  n := 10;

  WriteLn('Fibonacci rekurencyjnie (0..9):');
  for i := 0 to n - 1 do
    WriteLn(FibRekurencyjnie(i));

  WriteLn('Fibonacci iteracyjnie (0..9):');
  a := 0;
  b := 1;
  for i := 0 to n - 1 do
  begin
    WriteLn(a);
    tmp := a + b;
    a := b;
    b := tmp;
  end;
end.