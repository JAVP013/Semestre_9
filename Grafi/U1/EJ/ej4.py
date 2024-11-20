def f(x):
    return round(-x/2)


x = -7
while x < 7:
    print(x, (f(x)))
    x += 1
