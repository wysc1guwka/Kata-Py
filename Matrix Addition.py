def matrix_addition(a, b):
    c = []
    for x in range(0, len(a)):
        c.append([])
        for y in range(0, len(a[x])):
            c[x].append(a[x][y]+b[x][y])
    return c
