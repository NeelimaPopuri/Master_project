class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # str is meant for user-friendly output
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    # repr is meant for a more detailed, unambiguous output
    # repr is debugging
    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, year={self.year})"


# create an instance of the car class
my_car = Car('Hundai', 'Sonata', '2013')

# Usage
print(str(my_car))
print(repr(my_car))
