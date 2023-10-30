import unittest
from serviceable import Serviceable
from car_factory import CarFactory
from datetime import datetime

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Serviceable.needs_service(car))

   
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Serviceable.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))   

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Serviceable.needs_service(car))

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Serviceable.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissage(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(Serviceable.needs_service(car))

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(Serviceable.needs_service(car))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        warning_light_is_on = True

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(Serviceable.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(Serviceable.needs_service(car))


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Serviceable.needs_service(car))
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Serviceable.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))


        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Serviceable.needs_service(car))

if __name__ == '__main__':
    unittest.main()
