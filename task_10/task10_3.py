
class Figure:
    def __init__(self, color, size):
        self.color = color
        self.size = size

class Square(Figure):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __repr__(self):
        return self.color+' '+self.size+' '+'square'


class Circle(Figure):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __repr__(self):
        return self.color + ' ' + self.size + ' ' + 'circle'



box = [Square('yellow', 'medium'), Circle('blue', 'small')]
box.append(Square('red', 'big'))
print(box)

print(isinstance(box[1], Square))