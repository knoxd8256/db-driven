# Car Class - an example for defining a class in Python
# From Gaddis "Getting started with Python" 3rd Ed. p. 471

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "Make is %s, Model is %s, Year is %4d\n" % (self.make, self.model, self.year)



'''  Unit Test '''
if __name__ == "__main__":
    car = Car('Honda', 'Civic', 2016)
    print(car)


