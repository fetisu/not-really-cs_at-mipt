from math import sin, cos


def prime_numbers():
    primes = [2]

    for i in range(3, 2001):
        if_prime = True
        for j in primes:
            if i % j == 0:
                if_prime = False
                break
        if if_prime:
            primes.append(i)

    return primes


def selection_sort(what_to_sort=list):
    starter_x = what_to_sort[0]
    minx = what_to_sort[0]
    x_position = 0

    if len(what_to_sort) > 1:
        for i in range(1, len(what_to_sort)):
            looking_now = what_to_sort[i]

            if looking_now < minx:
                minx = looking_now
                x_position = i

        if x_position != 0:
            what_to_sort[0], what_to_sort[x_position] = minx, starter_x

        almost_sorting_result = selection_sort(what_to_sort[1:len(what_to_sort)])
        sorting_result = [minx]
        for i in range(len(almost_sorting_result)):
            sorting_result.append(almost_sorting_result[i])

    else:
        sorting_result = what_to_sort

    return sorting_result


def rotating_square(vertexes=list, alpha=int):
    x0 = (vertexes[0][0] + vertexes[2][0]) / 2
    y0 = (vertexes[0][1] + vertexes[2][1]) / 2

    alpha_cos = cos(alpha)
    alpha_sin = sin(alpha)

    vertexes1 = []

    for vertex in vertexes:
        dx = vertex[0] - x0
        dy = vertex[1] - y0

        x1 = x0 + dx * alpha_cos + dy * alpha_sin
        y1 = y0 + dx * (-alpha_sin) + dy * alpha_cos

        vertexes1.append(tuple([x1, y1]))

    return vertexes1


def money_money(available=int, prices=dict):
    can_afford = []

    for item in prices:
        if prices[item] <= available:
            can_afford.append(item)

    return can_afford


def five_have_no_idea_how_to_name_it(list_to_set=list):
    return list(set(list_to_set))


def number_six(a=set, b=set):
    return a - b
