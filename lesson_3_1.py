# lesson 3

# list find:
people = [
    ['Ivan Semenov', 'm', 1990, 180, 85],
    ['Petr Popov', 'm', 1980, 176, 89],
    ['Tatyana Ivanova', 'w', 1987, 165, 54],
    ['Dmitriy Petrov', 'm', 1981, 200, 110],
    ['Olga Olgina', 'w', 1970, 174, 65]
]

print('Список людей:')
for n in range(len(people)):
    print(n+1, end='    ')
    print(', '.join(str(i) for i in people[n]))

# Критерий выбора персоны:
max = ['Самый младший', 'Самый высокий', 'Самый тяжелый']
print('')
print('Выбор критерия поиска персоны:')
print (f'    {max[0]} -  1')
print (f'    {max[1]} -  2')
print (f'    {max[2]} -  3')
ind = int(input('Выберите критерий :   ')) + 1
if ind < 2 or ind > 4:
    print('Такого критерия нет!')

ind_max = 0
pers_max = []
for pers in people:
    if pers[ind] > ind_max:
        ind_max = pers[ind]
        pers_max = pers

print(' ')
print(max[ind-2], pers_max[0], ':  ', ind_max)
