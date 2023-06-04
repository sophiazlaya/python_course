class Library:

    def __init__(self, author, title, num, owner):
        self.author = author
        self.title = title
        self.__num_of_copies = num
        self.__owner = owner

    def __get_full_info(self, password):
        library_admission = '589'
        if password == library_admission:
            print('number of copies in the library:', self.__num_of_copies, '\n', 'owners:', self.__owner)
        else:
            print('Wrong password')

    def get_info(self):
        print('author:', self.author, '\n', 'title:', self.title)
        self.__get_full_info(input('Enter the password for full admission: '))

    def set_NumOfCop(self):
        self.__num_of_copies -= 1

    def get_book(self, owner):
        if self.__num_of_copies >= 1:
            self.set_NumOfCop()
            self.__owner.append(owner)

    def set_NewOwner(self, name1, name2):
        if (name1 != name2) and (name2 not in self.__owner):
            self.__owner[self.__owner.index(name1)] = name2


book1 = Library('Ыix of ravens', 'Love&hate', 3, [])
book1.get_book('Eva Evans')
book1.get_book('Ann Jane')
book1.get_info()
book1.set_NewOwner('Ann Jane', 'Alice')
book1.get_info()
