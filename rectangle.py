from shape import shape
from math import sqrt

class Rectangle(shape):
    def __init__(self,length, width):
            self.length = length
            self.width = width
            
    def area(self):
        a = self.length * self.width
        return a
            
    def perimeter(self):
        p = 2 * (self.length + self.width)
        return p
    
    def shape_detail(self):
        d = f'''
        length : {self.length}
        width : {self.width}
        area : { self.area()}
        perimeter : {self.perimeter()}
        diagonal " {self.diagonal()}
        '''
        print(d)
    
    def diagonal(self):
        dia = sqrt((self.length **2 + self.width **2))
        return dia
        
        
r = Rectangle(20,10)
r.shape_detail()