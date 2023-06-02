
class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)

class Kitchen(Table):
    def howplaces(self,n):
        if n < 2:
            print ("It is not kitchen table")
        else:
            self.places = n
    def outplases(self):
        print (self.places)


class Subject(Table):
    def add_tablecloth(self):
        if(self.long*self.width) > 2:
            print('there is tablecloth on the table')

    def tablecloth_choosing(self):
        print('tablecloth height = ', self.height-100)



ex = Subject(150, 100, 100)
ex.add_tablecloth()
ex.tablecloth_choosing()

