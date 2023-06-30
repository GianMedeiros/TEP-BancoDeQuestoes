# https://vjudge.net/contest/564977#problem/A

def resposta(res):
  
  print(res)

res = 0

dia = input()

semana = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

if dia == "SUN":
  resposta(7)
else:
  for i in semana:
    if i != dia:
      res += 1
    else:
      resposta(7-res)

