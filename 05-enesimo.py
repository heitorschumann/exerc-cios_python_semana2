def n_termo(i, r, n):
    count = 1
    while count < n:
        i += r
        count += 1

    return i


print(n_termo(1, 1, 100))
print(n_termo(100, -1, 100))
print(n_termo(5, -5, 2))
