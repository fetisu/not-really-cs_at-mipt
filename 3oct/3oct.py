from math import sin, cos


def prime_numbers():
    primes = [2]

    for i in range(3, 2001):
        if_prime = True  # такие переменные-флаги обычно называются is_<VARNAME>, т.е. is_prime в данном случае
        # Опционально, но еще можно было выделить это в отдельную функцию, т.к. это вроде логически целостный кусок
        for j in primes:
            # можно не чекать все числа, чтобы гарантировать, что новое число простое. Подумай как.
            if i % j == 0:
                if_prime = False
                break
        if if_prime:
            primes.append(i)

    return primes

# 9/10


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
        '''
        Да, рекурсия это часто красивое решение, и ты молодец, что юзаешь и тренишься.
        Но часто оно не эффективное. У тебя есть присвоение элементам массива внутри функции,
        так что скорее всего по умолчанию массив будет передаваться по значению,
        а это значит, что в памяти будет пирамидка из примерно N^2 / 2 элементов
        вместо одной строки из N элементов. Ну и время на выделение этой памяти тоже нужно.
        '''

        sorting_result = [minx]  # можно делать так: new_list = [x] + your_list
        for i in range(len(almost_sorting_result)):
            sorting_result.append(almost_sorting_result[i])

    else:
        sorting_result = what_to_sort

    return sorting_result

# 9/10


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
        '''
        сори что я тогда хрень сказал про матрицу поворота.
        Проверим например на (1,0):
        при угле типо pi/4 вектор вдоль Ох должен повернуться вверх,
        т.е. обе координаты должны стать меньше 1 но остать больше 0.
        Если подставить твою матрицу, то получится так
        | c  s|   |1|   | c|
        |-s  c| * |0| = |-s|
        т.е. Y стал отрицательным. Так не должно быть. Значит на самом деле матрица
        |c  -s|
        |s   c|
        '''

        vertexes1.append(tuple([x1, y1]))

    return vertexes1

# 10/10


def money_money(available=int, prices=dict):
    can_afford = []

    for item in prices:  # попробуй сделать one-liner comprehension
        if prices[item] <= available:
            can_afford.append(item)

    return can_afford
# 10/10


def five_have_no_idea_how_to_name_it(list_to_set=list):
    return list(set(list_to_set))
# 10/10


def number_six(a=set, b=set):
    return a - b
# 10/10
