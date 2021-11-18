A = [3, 4, 2, 1, 0, 8, 9, -1, 100, 0]
min = max = A.pop()
i = 0
while A:
    a = A.pop()
    i += 1
    print(a)
    if a < min:
        min = a
        imin = i
    if a > max:
        max = a
        imax = i
print('min =', min, '   i =', imin)
print('max =', max, '   i =', imax)
