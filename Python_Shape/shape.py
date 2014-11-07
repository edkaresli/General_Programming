# this is a comment to ensure Git is working
class Shape:
    def __init__(self, name):
        """
        (str) --> none
        name ... name of shape object
        """
        self.name = name
        return 

    def draw(self):
        """
        virtual base method
        """
        print("Base method draw(), name = " + self.name)
        print()

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def draw(self):
        print("Circle method draw(), name = " + self.name + ", radius = " + str(self.radius))
        print()

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def draw(self):
        print("Square.draw(), name = " + self.name + ", side = " + str(self.side))
        print()

base = Shape('zhopa')
base.draw()
cir = Circle('ring', 3.7)
cir.draw()
rect = Square('kispis', 5.0)
rect.draw()

a = ''

while True:
    print("Enter type of object to construct or 'quit' to exit: ")
    a = input()
    if(a == 'quit'):
        print("Quitting, have a nice day.")
        print()
        break
    if(a == 'shape'):
        s = Shape(a)
        s.draw()
    elif(a == 'circle'):
        r = float(input("Enter radius: "))        
        s = Circle('circle', r)
        s.draw()
    elif(a == 'square'):
        d = float(input("Enter side: "))        
        s = Square("square", d)
        s.draw()
    else:
        print("Unknown type! Try again!")
        print()

