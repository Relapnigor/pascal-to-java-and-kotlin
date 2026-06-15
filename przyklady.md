# Przykłady

---
## Przykład 1 - Bubble sort

### Wejście
##### Pascal

```pascal
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

```

### Wyjście
##### Kotlin

```kotlin
var tab: Array<Int> = Array(11) { 0 }
var i: Int = 0
var j: Int = 0
var n: Int = 0
var tmp: Int = 0

fun main(args: Array<String>) {
	n = 10
	tab[1] = 64
	tab[2] = 34
	tab[3] = 25
	tab[4] = 12
	tab[5] = 22
	tab[6] = 11
	tab[7] = 90
	tab[8] = 5
	tab[9] = 77
	tab[10] = 1
	println("Tablica przed sortowaniem:");
	for (i in 1 .. n) {
		println(tab[i]);
	}
	for (i in 1 .. n - 1) {
		for (j in 1 .. n - i) {
			if (tab[j] > tab[j + 1]){
				tmp = tab[j]
				tab[j] = tab[j + 1]
				tab[j + 1] = tmp
			}
		}
	}
	println("Tablica po sortowaniu:");
	for (i in 1 .. n) {
		println(tab[i]);
	}
}

```
##### Java

```java
public class BubbleSort {
    static int[] tab = new int[11];
    static int i;
    static int j;
    static int n;
    static int tmp;

    public static void main(String[] args) {
        n = 10;
        tab[1] = 64;
        tab[2] = 34;
        tab[3] = 25;
        tab[4] = 12;
        tab[5] = 22;
        tab[6] = 11;
        tab[7] = 90;
        tab[8] = 5;
        tab[9] = 77;
        tab[10] = 1;
        System.out.println("Tablica przed sortowaniem:");
        for (i = 1; i <= n; i++) {
            System.out.println(tab[i]);
        }
        for (i = 1; i <= n - 1; i++) {
            for (j = 1; j <= n - i; j++) {
                if (tab[j] > tab[j + 1]) {
                    tmp = tab[j];
                    tab[j] = tab[j + 1];
                    tab[j + 1] = tmp;
                }
            }
        }
        System.out.println("Tablica po sortowaniu:");
        for (i = 1; i <= n; i++) {
            System.out.println(tab[i]);
        }
    }
}

```

---
## Przykład 2 - Fibonacci

### Wejście
##### Pascal

```pascal
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
```

### Wyjście
##### Kotlin

```kotlin
var i: Int = 0
var n: Int = 0
var a: Int = 0
var b: Int = 0
var tmp: Int = 0

fun FibRekurencyjnie(n_arg: Int): Int{
	var n = n_arg
	if (n <= 1){
		return n
	}
	return FibRekurencyjnie(n - 1) + FibRekurencyjnie(n - 2)
}
fun main(args: Array<String>) {
	n = 10
	println("Fibonacci rekurencyjnie (0..9):");
	for (i in 0 .. n - 1) {
		println(FibRekurencyjnie(i));
	}
	println("Fibonacci iteracyjnie (0..9):");
	a = 0
	b = 1
	for (i in 0 .. n - 1) {
		println(a);
		tmp = a + b
		a = b
		b = tmp
	}
}

```

##### Java

```java
public class Fibonacci {
    static int i;
    static int n;
    static int a;
    static int b;
    static int tmp;

    public static int FibRekurencyjnie(int n) {
        if (n <= 1) {
            return n;
        }
        return FibRekurencyjnie(n - 1) + FibRekurencyjnie(n - 2);
    }

    public static void main(String[] args) {
        n = 10;
        System.out.println("Fibonacci rekurencyjnie (0..9):");
        for (i = 0; i <= n - 1; i++) {
            System.out.println(FibRekurencyjnie(i));
        }
        System.out.println("Fibonacci iteracyjnie (0..9):");
        a = 0;
        b = 1;
        for (i = 0; i <= n - 1; i++) {
            System.out.println(a);
            tmp = a + b;
            a = b;
            b = tmp;
        }
    }
}

```
---
## Przykład 3 - NWD i NWW

### Wejście
##### Pascal

```pascal
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
```

### Wyjście
##### Kotlin

```kotlin
var a: Int = 0
var b: Int = 0
var wynikNWD: Int = 0
var wynikNWW: Int = 0

fun NWD(a_arg: Int, b_arg: Int): Int{
	var a = a_arg
	var b = b_arg
	var tmp: Int
	while (b != 0) {
		tmp = b
		b = a % b
		a = tmp
	}
	return a
}
fun main(args: Array<String>) {
	a = 48
	b = 18
	println("Liczba A:");
	println(a);
	println("Liczba B:");
	println(b);
	wynikNWD = NWD(a, b)
	println("NWD:");
	println(wynikNWD);
	wynikNWW = (a * b / wynikNWD).toInt()
	println("NWW:");
	println(wynikNWW);
}

```

##### Java

```java
public class NwdNww {
    static int a;
    static int b;
    static int wynikNWD;
    static int wynikNWW;

    public static int NWD(int a, int b) {
        int tmp;
        while (b != 0) {
            tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }

    public static void main(String[] args) {
        a = 48;
        b = 18;
        System.out.println("Liczba A:");
        System.out.println(a);
        System.out.println("Liczba B:");
        System.out.println(b);
        wynikNWD = NWD(a, b);
        System.out.println("NWD:");
        System.out.println(wynikNWD);
        wynikNWW = (int)(a * b / wynikNWD);
        System.out.println("NWW:");
        System.out.println(wynikNWW);
    }
}

```

---
## Przykład 4 - Palindrom liczba

### Wejście
##### Pascal

```pascal
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
```
### Wyjście
##### Kotlin

```kotlin
var liczba: Int = 0
var oryginal: Int = 0
var odwrocona: Int = 0
var cyfra: Int = 0

fun main(args: Array<String>) {
	liczba = 12321
	oryginal = liczba
	odwrocona = 0
	while (liczba > 0) {
		cyfra = liczba % 10
		odwrocona = odwrocona * 10 + cyfra
		liczba = (liczba / 10).toInt()
	}
	println("Liczba oryginalna:");
	println(oryginal);
	println("Liczba odwrocona:");
	println(odwrocona);
	if (oryginal == odwrocona){
		println("To jest palindrom!");
	}
	else{
		println("To nie jest palindrom.");
	}
}

```

##### Java

```java
public class Palindrom {
    static int liczba;
    static int oryginal;
    static int odwrocona;
    static int cyfra;

    public static void main(String[] args) {
        liczba = 12321;
        oryginal = liczba;
        odwrocona = 0;
        while (liczba > 0) {
            cyfra = liczba % 10;
            odwrocona = odwrocona * 10 + cyfra;
            liczba = (int)(liczba / 10);
        }
        System.out.println("Liczba oryginalna:");
        System.out.println(oryginal);
        System.out.println("Liczba odwrocona:");
        System.out.println(odwrocona);
        if (oryginal == odwrocona) {
            System.out.println("To jest palindrom!");
        } else {
            System.out.println("To nie jest palindrom.");
        }
    }
}

```
---
## Przykład 5 - Selection sort

### Wejście
##### Pascal

```pascal
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
```

### Wyjście
##### Kotlin

```kotlin
var tab: Array<Int> = Array(9) { 0 }
var i: Int = 0
var j: Int = 0
var n: Int = 0
var minIdx: Int = 0
var tmp: Int = 0

fun main(args: Array<String>) {
	n = 8
	tab[1] = 29
	tab[2] = 10
	tab[3] = 14
	tab[4] = 37
	tab[5] = 13
	tab[6] = 4
	tab[7] = 99
	tab[8] = 2
	println("Przed sortowaniem:");
	for (i in 1 .. n) {
		println(tab[i]);
	}
	for (i in 1 .. n - 1) {
		minIdx = i
		for (j in i + 1 .. n) {
			if (tab[j] < tab[minIdx]){
				minIdx = j
			}
		}
		if (minIdx != i){
			tmp = tab[i]
			tab[i] = tab[minIdx]
			tab[minIdx] = tmp
		}
	}
	println("Po sortowaniu:");
	for (i in 1 .. n) {
		println(tab[i]);
	}
}

```
##### Java

```java
public class SelectionSort {
    static int[] tab = new int[9];
    static int i;
    static int j;
    static int n;
    static int minIdx;
    static int tmp;

    public static void main(String[] args) {
        n = 8;
        tab[1] = 29;
        tab[2] = 10;
        tab[3] = 14;
        tab[4] = 37;
        tab[5] = 13;
        tab[6] = 4;
        tab[7] = 99;
        tab[8] = 2;
        System.out.println("Przed sortowaniem:");
        for (i = 1; i <= n; i++) {
            System.out.println(tab[i]);
        }
        for (i = 1; i <= n - 1; i++) {
            minIdx = i;
            for (j = i + 1; j <= n; j++) {
                if (tab[j] < tab[minIdx]) {
                    minIdx = j;
                }
            }
            if (minIdx != i) {
                tmp = tab[i];
                tab[i] = tab[minIdx];
                tab[minIdx] = tmp;
            }
        }
        System.out.println("Po sortowaniu:");
        for (i = 1; i <= n; i++) {
            System.out.println(tab[i]);
        }
    }
}

```
---
## Przykład 6 - Sito Eratostenesa

### Wejście
##### Pascal

```pascal
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
```

### Wyjście
##### Kotlin

```kotlin
var sito: Array<Int> = Array(100) { 0 }
var i: Int = 0
var j: Int = 0
var n: Int = 0

fun main(args: Array<String>) {
	n = 50
	for (i in 1 .. n) {
		sito[i] = 1
	}
	sito[1] = 0
	i = 2
	while (i * i <= n) {
		if (sito[i] == 1){
			j = i * i
			while (j <= n) {
				sito[j] = 0
				j = j + i
			}
		}
		i++
	}
	println("Liczby pierwsze do 50:");
	for (i in 2 .. n) {
		if (sito[i] == 1){
			println(i);
		}
	}
}

```

##### Java

```java
public class SitoEratostenesa {
    static int[] sito = new int[100];
    static int i;
    static int j;
    static int n;

    public static void main(String[] args) {
        n = 50;
        for (i = 1; i <= n; i++) {
            sito[i] = 1;
        }
        sito[1] = 0;
        i = 2;
        while (i * i <= n) {
            if (sito[i] == 1) {
                j = i * i;
                while (j <= n) {
                    sito[j] = 0;
                    j = j + i;
                }
            }
            i++;
        }
        System.out.println("Liczby pierwsze do 50:");
        for (i = 2; i <= n; i++) {
            if (sito[i] == 1) {
                System.out.println(i);
            }
        }
    }
}

```


