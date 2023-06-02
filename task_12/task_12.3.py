class AutoCard:
    def __init__(self, name, surname, auto_group):
        self.name = name
        self.surname = surname
        self.__auto_group = auto_group

    def __get_info(self):
        return self.__auto_group

    def instructor(self):
        if self.__get_info() == 1:
            print('Grey')
        if self.__get_info() == 2:
            print('White')
        if self.__get_info() == 3:
            print('Croft')


Ann = AutoCard('Ann', 'Eliot', 'B')
Ann.instructor()

