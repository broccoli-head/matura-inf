def przestaw(n):
  global licznik
  licznik += 1

  r = n % 100
  a = r // 10
  b = r % 10
  n = n // 100
  if n > 0:
    w = a + 10 * b + 100 * przestaw(n)
  else:
    if a > 0:
      w = a + 10 * b
    else:
      w = b
  
  return w


# zad 1.3
def przestaw2(n):
  w = 0
  iteracja = 1

  while n > 0:
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    if w == 0:
      w = 10 * b + a
    else:
      iteracja *= 100
      if n == 0:
        w = iteracja * b + w
      else:
        w = iteracja * (10 * b + a) + w
  
  return w


def start(n):
  global licznik
  licznik = 0
  print(przestaw(n), licznik)
  print(przestaw2(n))


def main():
  print("zad 1.1")
  start(31649812)
  start(43657688)
  start(154005710)
  start(998877665544321)

main()