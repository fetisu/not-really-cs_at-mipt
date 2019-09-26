from graph import brushColor, penColor, circle, run, rectangle, polygon

mod = -1
x = 150
y = 100


def sheep(x, y, n):
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
    rectangle(x, + n / 2 + y, x + n*mod, y - n * (1 / 2))
    polygon(coordintes)
    brushColor('grey')
    circle(x + mod * n/4, y - 0.25*n, n // 6)
    brushColor("light grey")
    penColor("light grey")
    circle(x + (n + n // 7)*mod, y - 1.5*n, n // 8)
    circle(x + (n + n // 2)*mod, y - 2.0 * n, n // 7)
    circle(x + mod * 2.2*n, y - 2.5 * n, n // 6)


sheep(200, 300, 80)


run()
