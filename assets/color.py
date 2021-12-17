import random

# retorna uma cor
def getColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    cor = f'rgb({r},{g},{b})'
    return cor