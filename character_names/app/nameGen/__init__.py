from .names import names
from .titles import titles
from .descriptors import descriptors
import random
def generate():
    return random.choice(names) + ' ' + random.choice(titles) + ' the ' + random.choice(descriptors)
def arrGen(x):
    array = []
    i = 0
    while i < x:
        array.append(generate())
        i += 1
    return array