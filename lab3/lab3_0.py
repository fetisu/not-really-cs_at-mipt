from graph import windowSize, brushColor, penColor,\
    circle, run, penSize, line

windowSize(400, 400)

# big and round body
penSize(10)
penColor(47, 79, 79)
brushColor(47, 79, 79)

circle(200, 200, 120)

# dark circles for ears, circles under eyes and for the beauty
brushColor(40, 61, 61)

circle(125, 215, 40)
circle(275, 215, 35)
circle(210, 115, 15)
circle(270, 79, 34)
circle(130, 79, 34)
circle(260, 162, 30)

# eyes
brushColor('white')

circle(140, 165, 35)
circle(260, 165, 35)

# that thing inside eyes
brushColor(175, 133, 133)

circle(140, 165, 8)
circle(260, 165, 8)

# eyebrows
penColor(119, 78, 78)
penSize(15)

line(110, 135, 170, 140)
line(230, 145, 290, 125)


# mouth/moustache or how do u wanna call it
# by crossing over each other circles
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
