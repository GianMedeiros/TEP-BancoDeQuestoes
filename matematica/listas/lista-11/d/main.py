
n = int(input())

line = input()
frase = []
res = []
v = 0

for i in line:
  frase += i
  v = ord(i) + n
  if(v > 90):
    v = v - 26
  res += chr(v)

resposta = ""

for i in res:
  resposta += i

print(resposta)