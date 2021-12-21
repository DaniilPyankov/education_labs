class Group:
    def __init__(self, name, surname, birht_year, height, weight):
        self.name, self.surname, self.birht_year, self.height, self.weight = \
            name, surname, birht_year, height, weight
        print(f'person {self.name} {self.surname} created')

    def search_name(self, s_name):
        r_name = [s_name[i:i+3] for i in range(len(s_name))]
        count1, count2 = 0, 0
        for u_name in r_name:
            count1 += self.name.count(u_name)
            count2 += self.surname.count(u_name)
        # print(count/max(len(self.name), len(s_name)))
        if count1/max(len(self.name), len(s_name)) > 0.4 or count2/max(len(self.surname), len(s_name)) > 0.4:
            print(f'    {self.name, self.surname, self.birht_year, self.height, self.weight}')

    def search_year(self, s_year, u):
        if u == "младше":
            if self.birht_year > s_year - 2:
                print(f'    {self.name, self.surname, self.birht_year, self.height, self.weight}')

        elif u == "старше":
            if self.birht_year < s_year + 2:
                print(f'    {self.name, self.surname, self.birht_year, self.height, self.weight}')

        elif u == "ровно":
            if s_year - 1 < self.birht_year < s_year + 1:
                print(f'    {self.name, self.surname, self.birht_year, self.height, self.weight}')

people = [
    Group('Ivan', 'Semenov', 1990, 180, 130),
    Group('Petr', 'Popov', 1980, 176, 89),
    Group('Tatyana', 'Ivanova',1987, 165, 54),
    Group('Dmitriy', 'Petrov', 1981, 200, 105),
    Group('Olga', 'Olgina', 1970, 174, 65),
    Group('Ivan', 'Popov', 1988, 179, 95)
]

print('')
search_field = input('Введите поле поиска ( имя / фамилия / год ): ')

if search_field == 'имя' or search_field == 'фамилия':
    s_name = input('Поиск по ИМЕНИ / ФАМИЛИИ (ведите имя/фамилию или его часть): ')
    for person in people:
        person.search_name(s_name)

elif search_field == 'год':
    s_year = int(input('Поиск по году рождения (введите год поиска): '))
    u = input('Введите оператор сравнения ( старше / младше / ровно ): ')
    print(f'{u, s_year}:')
    for person in people:
        person.search_year(s_year, u)

else:
    print('Поле не задано')

print('Поиск закончен')
