from engine_new import Engine

from battery_new import Battery

class Car():
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery
    
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
    