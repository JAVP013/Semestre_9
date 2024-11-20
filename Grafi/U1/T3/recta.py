#  Indicamos el punto inical en (0,0), y solicitamos las coordenadas
#  le punto final (xf, yf)
xi, xf = 0, int(input("XF: "))
yi, yf = 0, int(input("YF: "))

# Cálculo de diferenciales
dx = xf - xi
dy = yf - yi


# Función para calcular y
def fx(xi, yi, xf, yf, x):
    return round((yf - yi) * (x - xi) / (xf - xi) + yi)


# Función para calcular x
def fy(xi, yi, xf, yf, y):
    return round((xf - xi) * (y - yi) / (yf - yi) + xi)


# Verificamos la pendiente para decidir el trazo
if abs(dx) >= abs(dy):
    # Pendiente menor a 45°
    if xi < xf:
        x = xi
        while x <= xf:
            print(f'({x},{fx(xi, yi, xf, yf, x)})')
            x += 1
    else:
        x = xi
        while x >= xf:
            print(f'({x},{fx(xi, yi, xf, yf, x)})')
            x -= 1
else:
    # # Pendiente mayor a 45°
    if yi < yf:
        y = yi
        while y <= yf:
            print(f'({fy(xi, yi, xf, yf, y)},{y})')
            y += 1
    else:
        y = yi
        while y >= yf:
            print(f'({fy(xi, yi, xf, yf, y)},{y})')
            y -= 1
