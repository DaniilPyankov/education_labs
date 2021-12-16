people = {
    'Ivan Semenov': {'г.р.': 1990, 'рост': 180, 'вес': 130},
    'Petr Popov': {'г.р.': 1980, 'рост': 176, 'вес': 89},
    'Tatyana Ivanova': {'г.р.': 1987, 'рост': 165, 'вес': 54},
    'Dmitriy Petrov': {'г.р.': 1981, 'рост': 200, 'вес': 105},
    'Olga Olgina': {'г.р.': 1970, 'рост': 174, 'вес': 65}
}

# вывод на печать списка
print('Список людей:')
n = 0
for key, value in people.items():
    n += 1
    print(n, key, value, sep='  ')

def my_find():
# ввод критерия выбора
    krit = [0, 'Самый старший', 'Самый высокий', 'Самый тяжелый']
    i = int(input(f'Введите критерий ({krit[1]} - 1, {krit[2]} - 2, {krit[3]} - 3):'))
    if i < 1 or i > 3:
        print('Неверный ввод критерия выбора')

    # сравнение элементов словаря по критерию
    ind = {1: 'г.р.', 2: 'рост', 3: 'вес'}

    if i == 1:
        ind_m = 3000
        for pers, info in people.items():
            if info[ind[i]] < ind_m:
                ind_m = info[ind[i]]
                pers_m = pers
    else:
        ind_m = 0
        for pers, info in people.items():
            if info[ind[i]] > ind_m:
                ind_m = info[ind[i]]
                pers_m = pers

    print(' ')
    print(f'{krit[i]} в списке {pers_m}. Его {ind[i]} {ind_m}')
my_find()
