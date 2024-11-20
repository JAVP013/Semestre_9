xi, yi = 0, 0
xf, yf = int(input("XF: ")), int(input("YF: "))

dx = xf - xi
dy = yf - yi

xk, yk = xi, yi
while yk <= yf:
    print(f'({xk},{yk})')
    DPk = 2*yk*dx + 2*dx - 2*xk*dy + 2*xi*dy - 2*yi*dx - dy
    if DPk >= 0:
        xk += 1
    yk += 1
