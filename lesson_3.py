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

# Выбор самого высокого:
height_max = 0
pers_max = []
for pers in people:
    if pers[3] > height_max:
        height_max = pers[3]
        pers_max = pers

print('')
print('Самый высокий - ', pers_max[0], ':  ', pers_max[3], 'см')
