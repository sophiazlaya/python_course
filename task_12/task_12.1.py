class MainInfo:
    def __init__(self, name, surname, date, number):
        self.name = name
        self.surname = surname
        self._dateofbirth = date
        self.__phonenumber = number


Eva = MainInfo('Eva', 'Evans', '25/08/2001', '+79930221728')

print(Eva.name)
print(Eva.surname)
print(Eva._dateofbirth)
print(Eva.__phonenumber)
