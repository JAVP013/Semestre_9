#  Indicamos el punto inicial en (0,0), y solicitamos las coordenadas del punto final (xf, yf)
xi, xf = 0, int(input("XF: "))
yi, yf = 0, int(input("YF: "))

# Calculo de diferenciales
dx = xf - xi
dy = yf - yi

# Variales e incrementos
x, y = xi, yi
inc_x, inc_y = 0, 0


# Función para redondear el pixel
def pixel(x, y):
    rx = round(x)
    ry = round(y)
    print(f'({rx},{ry})')


# Evaluación del diferencial
if abs(dx) >= abs(dy):
    pasos = abs(dx)
else:
    pasos = abs(dy)

# Procedimiento de calcular los pasos e incrementos
inc_x = dx/pasos
inc_y = dy/pasos
i = 0

# Ciclo para imprimir los pasos
while i <= pasos:
    pixel(x, y)

    x += inc_x
    y += inc_y
    i += 1