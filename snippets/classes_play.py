class Car:
    def __init__(self, make, model, year):
        self.make = str(make).title()
        self.model = str(model).title()
        self.year = int(year)
        if self.year < 1910 or self.year > 2026:
            raise ValueError("ERROR: Invalid year")
        
    def describe(self):
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        return self.describe()
    
    def __lt__(self, other):
        if self.make < other.make:
            return True
        elif self.make == other.make and self.model < other.model:
            return True
        return False
    
    def __eq__(self, other):
        return self.make == other.make and self.model == other.model and self.year == other.year

cars = [] 
cars.append(Car("Hyundai", "Sonata", 2010))
cars.append(Car("toyota", "prius", 2010))     
cars.append(Car("Volvo", "240", 1975))  
cars.append(Car("hyundai", "elantra", 2018))

print(sorted(cars, reverse=True))
    