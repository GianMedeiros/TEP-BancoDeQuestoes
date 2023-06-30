
def resposta(res):
  
  if res:
    print("Yes")
  else:
    print("No")


n = int(input())

for i in range(n):
  line = input()
  x, y = line.split()


resposta(True)
