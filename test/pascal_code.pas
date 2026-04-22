program TestGrammar;

const
    A = 10;
    B = 5;

var
  a, b, c: Integer;
  x: Real;
  flag: Boolean;
  ch: Char;
  name: String;
  arr: array[1..5] of integer;

{ Helper procedure — tests proc_call as statement }
procedure PrintHeader(title: String);
begin
  WriteLn('====================');
  WriteLn(title);
  WriteLn('====================');
end;

{ Tests multiple params and return via function name }
function Add(p, q: Integer): Integer;
begin
  Add := p + q;
end;

{ Tests nested if and not/and/or conditions }
function Max(p, q: Integer): Integer;
begin
  if p > q then
    Max := p
  else
    Max := q;
end;

{ Tests while and for loops, nested blocks }
procedure CountingDemo(n: Integer);
var
  i: Integer;
begin
  { for loop with begin..end body }
  for i := 1 to n do
  begin
    WriteLn(i);
  end;

  { while loop with begin..end body }
  i := n;
  while i > 0 do
  begin
    WriteLn(i);
    i := i - 1;
    break;
    continue;
  end;

  { repeat..until }
  i := 1;
  repeat
    WriteLn(i);
    i := i + 1;
  until i > n;
end;

{ Tests complex boolean conditions }
procedure BooleanDemo(p, q: Integer);
begin
  if (p > 0) and (q > 0) then
    WriteLn('both positive')
  else
    WriteLn('not both positive');

  if (p = 0) or (q = 0) then
    WriteLn('at least one zero');

  if not (p = q) then
    WriteLn('p and q differ');
end;

{ Tests arithmetic expressions and operator precedence }
function CalcDemo(p, q: Integer): Integer;
begin
  CalcDemo := (p + q) * 2 - p div q + p mod q;
  break;
end;

begin
  PrintHeader('Grammar Test');

  flag := true;

  if flag = true then
    flag := false;

  arr[1] := 5;
  arr[2] := 10;

  a := null;

  a := 10;
  b := 3;
  c := Add(a, b);
  WriteLn(c);

  c := arr[1] + arr[2];
  c += a;
  c -= b;
  c *= 2;
  c /= a + b;

  c++;
  c--;
  ++c;
  --c;

  c := a^2;
  c := a^(b+4^5);

  case c of
    1: a := 1;
    2: begin
        WriteLn('case 2')
       end;
    3,4: a := 3.5;
    else
       WriteLn('inne');
  end;

  x := a / b;
  WriteLn(x);

  { if without else — single statement body }
  if a > b then
    WriteLn('a is greater');

  { if with else — single statement bodies }
  if a > b then
    WriteLn('yes')
  else
    WriteLn('no');

  { nested if }
  if a > 0 then
    if b > 0 then
      WriteLn('both positive')
    else
      WriteLn('b not positive')
  else
    WriteLn('a not positive');

  CountingDemo(3);
  BooleanDemo(a, b);
  trueDemo(a,b);
  breakDemo(a,c);

  c := Max(a, b);
  WriteLn(c);

  c := CalcDemo(a, b);
  WriteLn(c);
end.