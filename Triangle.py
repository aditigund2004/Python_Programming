from shape import shape
from math import sqrt
class Tringle(shape):
    def __init__(self,s1,s2,base):
        self.side1=s1
        self.side2=s2
        self.base=base
        
    def cal_heigth(self):
        B = self.base/2
        H = sqrt(self.side1 **2 - B**2)
        return H
        
    def area(self):
       self.cal_heigth()
       a = 0.5 * (self.base*H)
       return a
   
    def perimeter(self):
       p = self.side1 + self.side2 + self.base
       return p
    def shape_details(self):
        d = f'''
        
        side1 : {self.side1}
         side2 : {self.side2}
         base : {self.base}
         heigth : {self.cal_heigth()}
         area : {self.area()}
         perimetr : {self.perimeter()}
         
        '''
       

t1 = Tringle(30,40,50)
t1.shape_details()