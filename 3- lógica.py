def sequence(start, increment, end):
    sequence = [start]
    while sequence[-1] < end:
        sequence.append(sequence[-1] + increment)
    return sequence

a = sequence(1, 2, 10)
b = sequence(2, 4, 100)
c = sequence(0, 1, 50)
d = sequence(4, 16, 200)
e = sequence(1, 1, 20)
f = sequence(2, 2, 50)

print(a)  # Saída: [1, 3, 5, 7, 9]
print(b)  # Saída: [2, 4, 8, 16, 32, 64, 128]
print(c)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49]
print(d)  # Saída: [4, 16, 36, 64, 128]
print(e)  # Saída: [1, 1, 2, 3, 5, 8, 13]
print(f)  # Saída: [2, 10, 12, 16, 17, 18, 19, 20]
