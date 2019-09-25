from graph import *
import random
import math


def grabla(x1, y1, x2, y2):
    n = 5
    a = int(((x2 - x1)**2)**0.5//(x2-x1))
    penSize(15)
    colour = random.randint(-1, 1)
    penColor(112 + colour // 3, 66, 65)
    brushColor(112 + colour // 3, 66, 65)
    penSize(1)
    for i in range(x1, x2, a):
        n += random.random()*((-1)**i)
        if n > 9:
            n -= 1
        elif n < 3:
            n += 1

        yy1 = (y2-y1)*(i-x1)/(x2-x1) + y1
        colour += random.randint(-5, 4)
        penColor(112 + colour, 66, 65)
        brushColor(112 + colour, 66, 65)
        circle(i, yy1, n)

    tan = (yy1 - y1)/(x2-x1)

    alpha = 3.14/2 + math.atan(tan)

    bx = int(50 * math.sin(alpha))
    by = int(50 * math.cos(alpha))
    penSize(10)
    penColor(53, 50, 51)
    line(x2 + bx, yy1 + by, x2 - bx, yy1 - by)
    for i in range(x2 - bx, x2 + bx, 7):
        penSize(3)
        y = yy1 + by + by*(i-x2-bx)/bx
        penSize(5)
        penColor(53, 50, 51)
        line(i, y, i, y - 18)
        penSize(2)
        penColor(66, 63, 64)
        line(i-2, y, i-2, y - 17)


windowSize(500, 600)


R = 103
G = 113
B = 64
m = [[0] * 300 for i in range(250)]


for i in range(250):
    for j in range(300):
        if i == 0:
            if j == 0:
                m[i][j] = [R, G, B]
            else:
                R = m[i][j-1][0]
                G = m[i][j-1][1]
                B = m[i][j-1][2]
        else:
            if j == 0:
                R = m[i-1][j][0]
                G = m[i-1][j][1]
                B = m[i-1][j][2]
            else:
                R = (m[i-1][j][0] + m[i][j-1][0])//2
                G = (m[i-1][j][1] + m[i][j-1][1])//2
                B = (m[i-1][j][2] + m[i][j-1][2])//2

        R += random.randint(-6, 6)
        G += random.randint(-6, 6)
        B += random.randint(-6, 6)
        if R < 70:
            R += 6
        elif R > 135:
            R -= 6
        if G < 80:
            G += 6
        elif G > 143:
            G -= 6
        if B < 40:
            B += 6
        elif B > 94:
            B -= 6

        m[i][j] = [R, G, B]
        brushColor(R, G, B)
        penColor(R, G, B)
        rectangle(2*i, 2*j, 2*i + 2, 2*j + 2)


brushColor(112, 66, 65)
penColor(112, 66, 65)

n = 7 + int(random.random()* 10)
for i in range(n):
    x1 = int(random.random()*500)
    dif = 50 + int(random.random()*100)
    x2 = x1 + dif*(-1)**i

    y1 = int(random.random() * 600)
    dif = 50 + int(random.random() * 100)
    y2 = y1 + dif * (-1)**i

    grabla(x1, y1, x2, y2)

run()
