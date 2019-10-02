from graph import windowSize, brushColor, penColor,\
    rectangle, polygon, circle, run
from random import randint


def whether_matches_rgb(R, G, B, n, range_size):
    # checking whether RGB in [30, 255] and in the original color range

    if R < max(R0 - range_size, 30):
        R += n
    elif R > min(255, R0 + range_size):
        R -= n

    if G < max(G0 - range_size, 30):
        G += n
    elif G > min(255, G0 + range_size):
        G -= n

    if B < max(B0 - range_size, 30):
        B += n
    elif B > min(255, B0 + range_size):
        B -= n

    return R, G, B


def sheep(x, y, n, mod):
    # making at first a left directed(mod = 1)
    # or right directed(mod = -1) ship in [0, 3] coordinates
    # and only after everything making it n-size and at x,y

    ship_form_coordinates = []

    # making the nose of the sheep
    # but the translator says crazy englishmen call it just a bow
    for i in range(20):
        ship_form_coordinates.append([-i * mod / 20, 1 - (i / 20) ** 2])

    # making sure that despite rounding of squares
    # the bow will be higher than the back of the ship
    ship_form_coordinates.append([(-1) * mod, -0.05])

    # the back of the ship
    for i in range(20):
        ship_form_coordinates.append([(3 - i / 20) * mod, (i / 20) ** 2])

    # n-size
    for i in range(len(ship_form_coordinates)):
        ship_form_coordinates[i] = [n * ship_form_coordinates[i][0] + x,
                                    n * ship_form_coordinates[i][1] + y]

    # the pipe
    brushColor('red')
    penColor('black')
    rectangle(mod * n * (3 / 4) + x, y, mod * n + x, y - (2 / 2) * n)

    # basic form of the ship
    brushColor('light grey')
    rectangle(x, + n / 2 + y, x + n * mod, y - n * (1 / 2))
    polygon(ship_form_coordinates)

    # the window of the ship
    brushColor('grey')
    circle(x + mod * n/4, y - 0.25 * n, n//7)

    # steam or smoke or how do u wanna call it
    brushColor("light grey")
    penColor("light grey")
    circle(x + (n + n // 7) * mod, y - 1.5 * n, n // 8)
    circle(x + (n + n // 2) * mod, y - 2.0 * n, n // 7)
    circle(x + mod * 2.2*n, y - 2.5 * n, n // 6)


def the_wallpaper(r0, g0, b0):
    # making an array of RGB per square 2x2
    # the RGB is the mean of upper-left and upper-right neighbor +- random
    # to make horizontal clusters that look like waves
    # instead of diagonally clusters when going by lines

    rgb_array = [[0] * 500 for k in range(500)]

    for diagonal_number in range(1000):

        if diagonal_number > 499:
            number_of_lines_in_the_diagonal = 499 - (diagonal_number - 499)
        else:
            number_of_lines_in_the_diagonal = diagonal_number

        for almost_y in range(number_of_lines_in_the_diagonal, -1, -1):

            if diagonal_number > 499:
                x = diagonal_number - 499 +\
                    number_of_lines_in_the_diagonal - almost_y
                y = (499 - number_of_lines_in_the_diagonal) + almost_y
            else:
                x = diagonal_number - almost_y
                y = almost_y

            # for the first column and line just making them standard
            if x == 0:
                R, G, B = r0, g0, b0

            elif y == 499 or y == 0:
                R, G, B = r0, g0, b0

            else:
                R = (rgb_array[x-1][y-1][0] + rgb_array[x-1][y+1][0]) // 2
                G = (rgb_array[x-1][y-1][1] + rgb_array[x-1][y+1][1]) // 2
                B = (rgb_array[x-1][y-1][2] + rgb_array[x-1][y+1][2]) // 2

            R += randint(-10, 10)
            G += randint(-10, 10)
            B += randint(-10, 10)

            R, G, B = whether_matches_rgb(R, G, B, 10, 60)
            rgb_array[x][y] = [R, G, B]

            # drawing the square
            brushColor(R, G, B)
            penColor(R, G, B)
            rectangle(2 * x, 2 * y, 2 * x + 2, 2 * y + 2)


windowSize(500, 600)

R0 = 64
G0 = 159
B0 = 255

the_wallpaper(R0, G0, B0)

# finally making ships
number_of = randint(4, 8)
for i in range(number_of):
    sheep(randint(10, 450), randint(10, 490),
          randint(15, 40), randint(0, 1) * 2 - 1)

run()
