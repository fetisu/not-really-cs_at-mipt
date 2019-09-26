from graph import windowSize, brushColor, penColor,\
    rectangle, polygon, circle, run
import random


def sheep(x, y, n, mod):
    coordintes = []

    for i in range(20):
        coordintes.append([-i * mod / 20, 1 - (i / 20) ** 2])

    coordintes.append([3 * mod, 0])

    for i in range(20):
        coordintes.append([(3 - i / 20) * mod, (i / 20) ** 2])

    for i in range(len(coordintes)):
        coordintes[i] = [n * coordintes[i][0] + x, n * coordintes[i][1] + y]

    brushColor('red')
    penColor('black')
    rectangle(mod * n * (3 / 4) + x, y, mod * n + x, y - (2 / 2) * n)
    brushColor('light grey')
    rectangle(x, + n / 2 + y, x + n * mod, y - n * (1 / 2))
    polygon(coordintes)
    brushColor('grey')
    circle(x + mod * n/4, y - 0.25*n, n//6)
    brushColor("light grey")
    penColor("light grey")
    circle(x + (n + n // 7)*mod, y - 1.5 * n, n // 8)
    circle(x + (n + n // 2)*mod, y - 2.0 * n, n // 7)
    circle(x + mod * 2.2*n, y - 2.5 * n, n // 6)


windowSize(500, 600)


R0 = 64
G0 = 159
B0 = 255
m = [[0] * 500 for i in range(500)]


# diagonally_wallpaper
for i in range(1000):
    a = i

    if i > 499:
        a = 499 - (i - 499)

    for j in range(a, -1, -1):
        x = i - j
        y = j
        if i > 499:
            x = i - 499 + a - j
            y = (499 - a) + j
        if x == 0:
            R = R0
            G = G0
            B = B0
        else:
            if y == 499 or y == 0:
                R = R0
                G = G0
                B = B0
            else:
                R = (m[x-1][y-1][0] + m[x-1][y+1][0]) // 2
                G = (m[x-1][y-1][1] + m[x-1][y+1][1]) // 2
                B = (m[x-1][y-1][2] + m[x-1][y+1][2]) // 2
        R += random.randint(-10, 10)
        G += random.randint(-10, 10)
        B += random.randint(-10, 10)

        if R < 34:
            R += 10
        elif R > 94:
            R -= 10
        if G < 119:
            G += 10
        elif G > 199:
            G -= 10
        if B < 205:
            B += 10
        elif B > 255:
            B -= 10

        m[x][y] = [R, G, B]
        brushColor(R, G, B)
        penColor(R, G, B)
        rectangle(2 * x, 2 * y, 2 * x + 2, 2 * y + 2)


number_of = random.randint(4, 8)
for i in range(number_of):
    sheep(random.randint(10, 450), random.randint(10, 490),
          random.randint(15, 40), random.randint(0, 1) * 2 - 1)


run()
