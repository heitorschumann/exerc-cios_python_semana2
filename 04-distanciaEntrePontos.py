import math


def distancia(x1, y1, x2, y2):
    D = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return D


x1, y1, x2, y2 = map(int, input().split())
print(distancia(x1, y1, x2, y2))
