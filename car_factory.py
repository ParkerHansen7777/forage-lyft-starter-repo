from car_new import Car

from capulet_engine_new import CapuletEngine
from willoughby_engine_new import WilloughbyEngine
from sternman_engine_new import SternmanEngine
from spindler_battery_new import SpindlerBattery
from nubbin_battery_new import NubbinBattery


class CarFactory():
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
        
    def create_glissage(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
        
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(last_service_date, current_date))
        
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))
        
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))

