from graph import *

windowSize(400, 400)

penSize(10)
penColor(47, 79, 79)
brushColor(47, 79, 79)

circle(200, 200, 120)

brushColor(40, 61, 61)

circle(125, 215, 40)
circle(275, 215, 35)
circle(210, 115, 15)
circle(270, 79, 34)
circle(130, 79, 34)
circle(260, 162, 30)

brushColor('white')

circle(140, 165, 35)
circle(260, 165, 35)

brushColor(175, 133, 133)

circle(140, 165, 8)
circle(260, 165, 8)

x = 140
y = 240
n = 20

penColor(119, 78, 78)
penSize(15)

line(110, 135, 170, 140)
line(230, 145, 290, 125)

x = 140
y = 260
n = 5
brushColor(119, 78, 78)

for i in range(7):
    circle(x, y, n)
    x += 8
    y -= 5**(i**0.2)
    n += 2

for i in range(8):
    circle(x, y, n)
    x += 10
    y += 5**(i**0.2)
    n -= 2

run()
