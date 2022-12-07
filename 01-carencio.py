import math
# D <= 100 = é o amor da minha vida
# 100 < D && D <= 200 = talvez de certo
# D > 200 = não vale a pena investir

# x1, y1, x2, y2 = map(int, input().split())
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

D = ((x2 - x1) ** 2 + (y2 - y1) ** 2) * 0.5
# D = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if D <= 100:
    print("É o amor da minha vida")
elif D > 100 and D <= 200:
    print("Talvez dê certo")
elif D > 200:
    print("Não vale a pena investir")
