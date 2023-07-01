
def resposta(vet):
  for i in vet:
    print(i)

n = int(input())

vet = []
res = 0

for i in range(n):
  line = input()
  x, y = line.split()
  x = int(x)
  y = int(y)

  if x == y:
    vet.append(0)
  else:
    if x > y:
      res = x-y
    else:
      res = y-x

    if res > 99:
      k_txt = ""
      k = int(res/100)
      k_txt = str(k)
      resto = res%100
      if resto != 0:
        if resto > 9:
          k = int(res/10)
          if res%10 != 0:
            k += 1

          k_txt += str(k)
          vet.append(k)

        else:
          k_txt += '1'
          vet.append(k_txt)
      else:
        k_txt += '0'
        vet.append(k_txt)

    elif res > 9:
      k = int(res/10)
      if res%10 != 0:
        k += 1

      vet.append(k)

    else:
      vet.append(1)

resposta(vet)
