from engine_new import Engine
from battery_new import Battery
from tires import Tires

class Car():
    def __init__(self, Engine, Battery, Tires):
        self.engine = Engine
        self.battery = Battery
        self.tires = Tires
    
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service():
            return True
        else:
            return False
    