class student:
    """Создание конструктора с 5-ю параметрами: имя студента, название вуза, название факультета, курс и группа"""
    def __init__(self, student_name, univercity_name, faculty , course, group):
        self.student_name = student_name
        self.univercity_name = univercity_name
        self.faculty = faculty
        self.course = course
        self.group = group
    """Создание исходного текста с атрибутами класса"""
    def __str__(self):
        return f'Меня зовут {self.student_name} ' +\
            f'Я учусь в {self.univercity_name} ' +\
            f'на факультете {self.faculty} ' +\
            f'{self.course} курса' +\
            f'в группе {self.group}'

Student = student('Alex', 'ДГТУ', 'ФКТВТиЭ', '3', 'Y933') #Заданные перемннные
print(Student) #Вывод исходного текста