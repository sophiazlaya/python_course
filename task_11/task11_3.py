import time


def find(dic, text):
    for key in dic:
        if text in key:
            return dic[key]
    return None


dic = {
    ('Grey', 'White', 'Blue'): 'James Blue',
    ('Yellow', 'Pink', 'Orange'): 'Sam White'
}

time_now = int(time.strftime('%H'))


class Worker:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.work_hours = [9, 17]
        self.admission = 1

    def worker_info(self):
        print(self.name, self.surname)

    def admission_level(self):
        print('admission level -', self.admission)

    def whoismymanager(self):
        print(self.name, ', Ваш менеджер', find(dic, self.surname))

    def is_at_work(self):
        if (time_now >= self.work_hours[0]) and (time_now <= self.work_hours[1]):
            print(self.name, self.surname, 'должен быть на работе')
        else:
            print('это не его рабочее время')


class Manager(Worker):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.working_hours = [8, 19]
        self.admission = 2

    def access_level(self):
        super(Manager, self).admission_level()

    def is_at_work(self):
        super(Manager, self).is_at_work()


class Boss(Manager):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.working_hours = [10, 15]
        self.admission = 3

    def admission_level(self):
        super(Boss, self).admission_level()

    def is_at_work(self):
        super(Boss, self).is_at_work()


Anton = Worker('Anton', 'Smith')
Anton.worker_info()
Anton.admission_level()
Anton.whoismymanager()
Anton.is_at_work()

print('\n')
John = Manager('John', 'Armstrong')
John.worker_info()
John.admission_level()
John.is_at_work()

print('\n')
Ann = Boss('Ann', 'Cooper')
Ann.worker_info()
Ann.admission_level()
Ann.is_at_work()
