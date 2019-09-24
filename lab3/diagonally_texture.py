from graph import *
import random


windowSize(500, 600)


R = 79
G = 119
B = 134
m = [[0] * 300 for i in range(250)]


for i in range(250):
    for j in range(300):
        if i == 0:
            if j == 0:
                m[i][j] = [R, G, B]
        else:
            if j != 0:
                R = (m[i-1][j][0] + m[i][j-1][0])//2
                G = (m[i-1][j][1] + m[i][j-1][1])//2
                B = (m[i-1][j][2] + m[i][j-1][2])//2
                if i%25 == 0 and j%25 == 0:
                    R += 20
                    G += 20
                    B += 20
            else:
                R = 79
                G = 119
                B = 134
        R += random.randint(-5, 5)
        G += random.randint(-5, 5)
        B += random.randint(-5, 5)
        if R < 43:
            R += 5
        elif R > 103:
            R -= 5
        if G < 89:
            G += 5
        elif G > 149:
            G -= 5
        if B < 104:
            B += 5
        elif B > 164:
            B -= 5

        m[i][j] = [R, G, B]
        brushColor(R, G, B)
        penColor(R, G, B)
        rectangle(2*i, 2*j, 2*i + 2, 2*j + 2)


run()