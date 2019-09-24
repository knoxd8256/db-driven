from .names import names
from .titles import titles
from .descriptors import descriptors
import random
def generate():
    return random.choice(names) + ' ' + random.choice(titles) + ' ' + random.choice(descriptors)
def arrGen(x):
    i = 0
    array = []
    while (i < x):
        array.append(generate())
        i = i + 1
    return array