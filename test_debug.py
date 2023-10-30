from serviceable import Serviceable
from car_factory import CarFactory
from datetime import datetime


print("------calliope------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
current_mileage = 0
last_service_mileage = 0
tread = [.5,.5,.5,.5]

Car1 = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tread)


print(Car1.engine.needs_service())
print(Car1.battery.needs_service())
print(Car1.tires.needs_service())
print(Serviceable.needs_service(Car1))
print("---------------------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 1)
current_mileage = 0
last_service_mileage = 0
tread = [1,1,.5,.4]

Car1 = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tread)

print(Car1.engine.needs_service())
print(Car1.battery.needs_service())
print(Car1.tires.needs_service())
print(Serviceable.needs_service(Car1))
print("---------------------")

print("------glissade------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
current_mileage = 0
last_service_mileage = 0
tread = [.5,.9,.5,.5]

Car2 = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage, tread)

print(Car2.engine.needs_service())
print(Car2.battery.needs_service())
print(Car2.tires.needs_service())
print(Serviceable.needs_service(Car2))
print("---------------------")

