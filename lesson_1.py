# lesson 1

# change
a = 'xxxx zzzz yyyy'
b = ''
for i in a:
    if i == 'x':
        b += 'y'
    else:
        b += i
print(b)


# mult
s = [2, 3, 4, 5, 7, 9]
r = 1
for x in s:
    if x % 3 == 0 or x % 5 == 0:
        r *= x
print(r)

# replace
print('xxxx zzzz yyyy'.replace('x', 'y'))
