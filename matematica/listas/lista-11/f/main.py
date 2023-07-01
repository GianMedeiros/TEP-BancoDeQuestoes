
def resposta(valor):
  print(valor)

n = int(input())

total = 0
res = 0
valores = []
maior = 0

line = input()
valores = line.split()

for i in valores:
  i = int(i)
  total += i
  if maior < i:
    maior = i
  
res = (maior*n) - total

resposta(res)
