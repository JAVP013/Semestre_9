def fx(xi, yi, xf, yf, x):
    return round((yf-yi)*(x-xi)/(xf-xi)+yi)


def fy(xi, yi, xf, yf, y):
    return round((xf-xi)*(y-yi)/(yf-yi)+xi)


xi, yi = 0, 0
xf, yf = int(input("XF:")), int(input("YF:"))

y = yi
while y <= yf:
    print(f'({fy(xi,yi,xf,yf,y)},{y})')
    y += 1
