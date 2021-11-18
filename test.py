# Задача 1:
s = "abcdefghijklmnop"
while s != "":
  print(s)
  s = s[1:-1]

# Задача 2:
# for i in range(1,10):
#  for j in range(1,10):
#    print(' %2i' % (i*j), end='')
#  print()

# Задача 3
x = range(10)
print('')
print('Сумма ряда x = range(10):')
# for:
s = 0
for i in x:
    s += i
print('    for:   ', s)

# while:
s = 0
while x:
    s += x[0]
    x = x[1:]
print ('    while: ', s, end='\n\n')

# Задача 4
b = [20, 24, 26, 30]
print('Среднее значение ряда b = [20, 24, 26, 30]:')

# for:
s = 0
for x in b:
    s += x
print('   for:    ', s/len(b))

s = 0
l = len(b)
while b:
    s += b[0]
    b = b[1:]
print('   while:  ', s/l)
