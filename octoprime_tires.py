from abc import ABC

from tires import Tires

class OctoprimeTires(Tires, ABC):
    def __init__(self, tread):
        self.tread = tread
    
    def needs_service(self):
        sum = 0
        for tire in self.tread:
            sum += tire
        if sum >= 3:
            return True
        else:
            return False
            