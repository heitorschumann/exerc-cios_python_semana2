def imprimeTermos(n):
    x = n
    while x != 0:
        if x == 1:
            x -= 1
            print(x)
        else:
            x -= 2
            print(x)


imprimeTermos(int(input()))
