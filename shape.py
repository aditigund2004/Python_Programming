from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    
    
    # perimeter -> addition of all sides 