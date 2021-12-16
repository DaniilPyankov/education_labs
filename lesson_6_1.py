class Group:
    def __init__(self, name, surname, birht_year, height, weight):
        self.name, self.surname, self.birht_year, self.height, self.weight = \
            name, surname, birht_year, height, weight
        print(f'person {self.name} {self.surname} created')

people = [
    Group('Ivan', 'Semenov', 1990, 180, 130),
    Group('Petr', 'Popov', 1980, 176, 89),
    Group('Tatyana', 'Ivanova',1987, 165, 54),
    Group('Dmitriy', 'Petrov', 1981, 200, 105),
    Group('Olga', 'Olgina', 1970, 174, 65)
]

