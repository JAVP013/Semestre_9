r = int(input("RADIO: "))

x = 0
y = r
DPk = 3-2*r
while x <= y:

    print(f'({x},{y})')
    print(f'({-x},{y})')
    print(f'({x},{-y})')
    print(f'({-x},{-y})')
    print(f'({y},{x})')
    print(f'({-y},{x})')
    print(f'({y},{-x})')
    print(f'({-y},{-x})')
    if DPk >= 0:
        DPk += 4*(x-y)+10
        y -= 1
    else:
        DPk += 4*x+6
    x += 1
