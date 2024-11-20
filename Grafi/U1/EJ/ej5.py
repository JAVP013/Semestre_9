def f(xi, yi, xf, yf, x):
    return round((yf-yi)*(x-xi)/(xf-xi)+yi)


xi, yi = -1, 3
xf, yf = 5, 1

dx = xf-xi
dy = yf-yi
m = dy/dx

if 0 <= abs(m) <= 1:
    x = xi
    while x <= xf:
        print(x, f(xi, yi, xf, yf, x))
        x += 1
else:
    print("Pixeles discontinuos")
