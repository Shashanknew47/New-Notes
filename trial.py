import  math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius **2  * math.pi
    def __repr__(self):
        return f'{self.__class__.__name__} has area of {self.area}'
    

class Donut(Circle):
    def __init__(self,outer,inner):
        Circle.__init__(self,outer)
        self.inner = inner

    def area(self):
        outer,inner = self.radius,self.inner
        return Circle(outer).area() - Circle(inner).area()

D1 = Donut(5,2)
print(D1.area())

