program InstrukcjaCase;

var
  opcja    : integer;
  znak     : string;
  dzien    : integer;
  miesiac  : integer;
  wynik    : integer;
  nazwa    : string;

begin
  opcja := 2;

  { Podstawowy case z integer }
  case opcja of
    1: wynik := 10;
    2: wynik := 20;
    3: wynik := 30;
  end;

  { Case z else }
  case opcja of
    1: wynik := 100;
    2: wynik := 200;
    else wynik := 0;
  end;

  { Case z blokami begin-end }
  case opcja of
    1:
    begin
      wynik := 1;
      nazwa := 'jeden';
    end;
    2:
    begin
      wynik := 2;
      nazwa := 'dwa';
    end;
    3:
    begin
      wynik := 3;
      nazwa := 'trzy';
    end;
    else
    begin
      wynik := -1;
      nazwa := 'nieznany';
    end;
  end;

  { Case ze stringiem }
  znak := 'A';
  case znak of
    'A': wynik := 1;
    'B': wynik := 2;
    'C': wynik := 3;
    else wynik := 0;
  end;

  { Case z wyrazeniem }
  wynik := 0;
  case opcja * 2 of
    2: wynik := 1;
    4: wynik := 2;
    6: wynik := 3;
  end;

  { Zagniezdzony case }
  case opcja of
    1:
    begin
      case dzien of
        1: wynik := 11;
        2: wynik := 12;
        else wynik := 10;
      end;
    end;
    2:
    begin
      case miesiac of
        1: wynik := 21;
        2: wynik := 22;
        else wynik := 20;
      end;
    end;
    else wynik := 0;
  end;
end.
