def deivis_sequence(a):
    sequence = [1, 2, 2]
    count = 3
    if a <= 3:
        return sequence[a - 1]
    else:
        while len(sequence) < a:
            sequence.append(sequence[count - 1] + sequence[count - 2] - 1)
            count += 1
            # print(sequence)
    return sequence[a - 1]


print(deivis_sequence(2))
print(deivis_sequence(5))
print(deivis_sequence(10))
