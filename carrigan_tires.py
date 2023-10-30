from abc import ABC

from tires import Tires

class CarriganTires(Tires, ABC):
    def __init__(self, tread):
        self.tread = tread
    
    def needs_service(self):
        for tire in self.tread:
            if tire >= 0.9:
                return True
        return False
            