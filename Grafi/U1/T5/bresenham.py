xi, yi = 0, 0
xf = int(input("xf"))
yf = int(input("yf"))

dx = xf-xi
dy = yf-yi

xk, yk = xi, yi

while xk <= xf:
    print(xk, yk)
    # DPk = 2*xk*dy+2*dy-2*yk*dx+2*yi*dx-2*xi*dy-dx
    DPk = 2*dy-dx
    if DPk >= 0:
        yk += 1
    xk += 1
