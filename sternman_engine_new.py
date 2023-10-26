from abc import ABC

from engine_new import Engine

class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
    
    def needs_service(self):
        return self.warning_light_is_on