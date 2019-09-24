'''Author: David Knox\nDate Created: 9/17/2019\nDescription: A simple module defining the Product() class.\n'''

class Product:
    '''This class defines an object describing a product with a UID, decription, stock, and price.'''
    def __init__(self, prod, desc, units, price):
        '''This init method assigns all of the internal variables used in the Product class.'''
        self.prod = prod
        self.desc = desc
        self.units = units
        self.price = price
    def __str__(self):
        return "\n I.D. : %s\n Description : %s\n Stock : %s\n Price : %s\n" % (self.prod, self.desc, self.units, self.price)