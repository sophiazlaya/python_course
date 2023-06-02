
class Figure:
    def __init__(self):
        self.color = 'White'

    def change_color(self, new_color):
        self.color = new_color
        print('new color is', self.color)

    def info(self):
        pass

class Oval(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def info(self):
        print('It is an oval', 'one axis =', self.a, 'another axis =', self.b, 'color =', self.color)


class Square(Figure):
    def __init__(self, a):
        super().__init__()
        self.a = a


    def info(self):
        print('It is a square', 'side size =', self.a, 'color =', self.color)

ov = Oval(7, 11)
ov.info()
ov.change_color('Blue')
ov.info()
sq = Square(7)
sq.info()



