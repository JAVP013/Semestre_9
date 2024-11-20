import math
r = 10
x = -10


while x <= 10:
    y = round(math.sqrt(r**2-x**2))
    print(f'({x},{y})')
    x += 1
