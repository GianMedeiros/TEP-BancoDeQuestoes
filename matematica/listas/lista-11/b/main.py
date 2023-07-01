x = int(input())
frase = input()

def resposta(res):
  if not res:
    print("No")
  else:
    print("Yes")

res = True

if x%2 == 1:
  res = False
  resposta(False)
else:
  lista = []
  par1 = ""
  par2 = ""

  for i in frase:
    lista.append(i)

  metade = int(len(lista)/2)

  for i in range(metade):
    if lista[i] != lista[i+metade]:
      res = False
      resposta(False)

  if res:
    resposta(res)
