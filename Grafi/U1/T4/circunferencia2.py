import math
r = int(input("Radio: "))

# Arreglo de puntos generados
puntos = []

# arriba
x = round(-(r*math.sqrt(2))/2)
print(f'x = {-x}')
while x <= 0:
    y = round(math.sqrt(r**2-x**2))
    # print(f'({x},{y})')

    if abs(x) != abs(y):
        puntos.append((y, x))
        puntos.append((-y, x))
        puntos.append((-y, -x))
        puntos.append((y, -x))
    puntos.append((x, -y))
    puntos.append((-x, -y))
    puntos.append((-x, y))
    puntos.append((x, y))
    x = x+1

# print(len(puntos))
# print(puntos)
