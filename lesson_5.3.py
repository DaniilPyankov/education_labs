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

# Нечеткое сравнение имени:
n = input('Введите имя или фамилию: ')
ngrams = [n[i:i+3] for i in range(len(n))]
for person in people:
    count = 0
    for ngram in ngrams:
        count += person[0].count(ngram)
    print(count/max(len(n), len(person[0])))
