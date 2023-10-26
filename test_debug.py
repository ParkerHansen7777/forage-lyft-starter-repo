from serviceable import Serviceable
from car_factory import CarFactory
from datetime import datetime


print("------calliope------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
current_mileage = 0
last_service_mileage = 0

Car1 = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)


print(Car1.engine.needs_service())
print(Car1.battery.needs_service())
print(Serviceable.needs_service(Car1))
print("---------------------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 1)
current_mileage = 0
last_service_mileage = 0

Car1 = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)

print(Car1.engine.needs_service())
print(Car1.battery.needs_service())
print(Serviceable.needs_service(Car1))
print("---------------------")

today = datetime.today().date()
last_service_date = datetime.today().date()
current_mileage = 30001
last_service_mileage = 0

Car1 = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)

print(Car1.engine.needs_service())
print(Car1.battery.needs_service())
print(Serviceable.needs_service(Car1))
print("---------------------")

today = datetime.today().date()
last_service_date = datetime.today().date()
current_mileage = 30000
last_service_mileage = 0

Car1 = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)

print(Car1.engine.needs_service())
print(Car1.battery.needs_service())
print(Serviceable.needs_service(Car1))
print("---------------------")

print("------glissade------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
current_mileage = 0
last_service_mileage = 0

Car2 = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)

print(Car2.engine.needs_service())
print(Car2.battery.needs_service())
print(Serviceable.needs_service(Car2))
print("---------------------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 1)
current_mileage = 0
last_service_mileage = 0

Car2 = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)

print(Car2.engine.needs_service())
print(Car2.battery.needs_service())
print(Serviceable.needs_service(Car2))
print("---------------------")

today = datetime.today().date()
last_service_date = datetime.today().date()
current_mileage = 60001
last_service_mileage = 0

Car2 = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)

print(Car2.engine.needs_service())
print(Car2.battery.needs_service())
print(Serviceable.needs_service(Car2))
print("---------------------")

today = datetime.today().date()
last_service_date = datetime.today().date()
current_mileage = 60000
last_service_mileage = 0

Car2 = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)

print(Car2.engine.needs_service())
print(Car2.battery.needs_service())
print(Serviceable.needs_service(Car2))
print("---------------------")

print("------palindrome------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
warning_light_is_on = False

Car3 = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)

print(Car3.engine.needs_service())
print(Car3.battery.needs_service())
print(Serviceable.needs_service(Car3))
print("---------------------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 1)
warning_light_is_on = False

Car3 = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)

print(Car3.engine.needs_service())
print(Car3.battery.needs_service())
print(Serviceable.needs_service(Car3))
print("---------------------")

today = datetime.today().date()
last_service_date = today
warning_light_is_on = True

Car3 = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)

print(Car3.engine.needs_service())
print(Car3.battery.needs_service())
print(Serviceable.needs_service(Car3))
print("---------------------")

today = datetime.today().date()
last_service_date = today
warning_light_is_on = False

Car3 = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)

print(Car3.engine.needs_service())
print(Car3.battery.needs_service())
print(Serviceable.needs_service(Car3))
print("---------------------")

print("------rorschach------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 5)
current_mileage = 0
last_service_mileage = 0

Car4 = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

print(Car4.engine.needs_service())
print(Car4.battery.needs_service())
print(Serviceable.needs_service(Car4))
print("---------------------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
current_mileage = 0
last_service_mileage = 0

Car4 = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

print(Car4.engine.needs_service())
print(Car4.battery.needs_service())
print(Serviceable.needs_service(Car4))
print("---------------------")

today = datetime.today().date()
last_service_date = today
current_mileage = 60001
last_service_mileage = 0

Car4 = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

print(Car4.engine.needs_service())
print(Car4.battery.needs_service())
print(Serviceable.needs_service(Car4))
print("---------------------")

today = datetime.today().date()
last_service_date = today
current_mileage = 60000
last_service_mileage = 0

Car4 = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

print(Car4.engine.needs_service())
print(Car4.battery.needs_service())
print(Serviceable.needs_service(Car4))
print("---------------------")

print("------thovex------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 5)
current_mileage = 0
last_service_mileage = 0

Car5 = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)

print(Car5.engine.needs_service())
print(Car5.battery.needs_service())
print(Serviceable.needs_service(Car5))
print("---------------------")

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
current_mileage = 0
last_service_mileage = 0

Car5 = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)

print(Car5.engine.needs_service())
print(Car5.battery.needs_service())
print(Serviceable.needs_service(Car5))
print("---------------------")

today = datetime.today().date()
last_service_date = today
current_mileage = 30001
last_service_mileage = 0

Car5 = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)

print(Car5.engine.needs_service())
print(Car5.battery.needs_service())
print(Serviceable.needs_service(Car5))
print("---------------------")

today = datetime.today().date()
last_service_date = today
current_mileage = 30000
last_service_mileage = 0

Car5 = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)

print(Car5.engine.needs_service())
print(Car5.battery.needs_service())
print(Serviceable.needs_service(Car5))
print("---------------------")