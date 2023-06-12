for x in range(11):
    for y in range(11):
        if (x**3 + x + 6) %11 == y**2 %11:
            print(x, y)