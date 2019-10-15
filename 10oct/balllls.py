from tkinter import Tk, Canvas, StringVar, Label, Entry, END
from random import randrange as rnd, choice
from math import cos, sin

root = Tk()
width = 800
height = 630
root.geometry(str(width)+'x'+str(height))

# the game body
canvas_canvasov = Canvas(root, bg='#AFEEEE', width=width, height=600)
canvas_canvasov.place(x=0, y=0)

# nice colour of bottom board
canvas_down_background = Canvas(root, bg='#AFEEFF', width=width, height=30)
canvas_down_background.place(x=0, y=600)

# entry item and setting default name
entered_name = StringVar()
name_entry = Entry(root, width=20, textvariable=entered_name)
name_entry.insert(END, 'noname')
name_entry.place(x=325, y=605)

# text for bottom board
text = Label(root, text='Please, enter your name for the scores table:3')
text.place(x=10, y=605)
text_second = Label(root, text="and do it before scoring 50, or don't do at all")
text_second.place(x=500, y=605)

# basic design colours
ball_colors = ['#E6E6FA', '#F5FFFA', '#F0FFF0', '#FDF5E6',
               '#F4A460', '#E6E6FA', '#FFE4E1']
oval_colors = ['#DC143C', '#8B008B']

# looking at the file for best scores
scores_file = open('scores')
best_results = {}
for line in scores_file:
    persons_score = line.split()
    best_results[persons_score[0]] = persons_score[1]
scores_file.close()
lowest_best_score = 50

# all the global variables
number_of_wins = 0
balls = []
ovals = []
balls_mods = []
balls_coords = []
how_long_the_same_set = 1000
timer_time = 5

# explaining the game text
canvas_canvasov.create_text(150, 50, text='Hi there. This game is very simple \n'
                                          'Every click inside a ball is a meow \n'
                                          'The more meows the better')


def new_set():
    """deleting previous balls and ovals and making new ones"""
    global balls, ovals, balls_mods

    # clearing the field
    for ball in balls:
        canvas_canvasov.delete(ball)
    for oval in ovals:
        canvas_canvasov.delete(oval)

    balls = []
    balls_mods = []
    ovals = []

    # new random number of balls
    for i in range(rnd(4, 12)):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(20, 40)
        balls.append(canvas_canvasov.create_oval(x - r, y - r, x + r, y + r,
                                                 fill=choice(ball_colors), width=0))
        balls_mods.append([rnd(-3, 3), rnd(-3, 3)])

    # new zero or some ovals
    for i in range(rnd(0, 2)):
        x = rnd(100, 700)
        y = rnd(100, 500)
        dx = rnd(5, 20)
        dy = rnd(5, 20)
        ovals.append(canvas_canvasov.create_oval(x, y, x + dx, y + dy,
                                                 fill=choice(oval_colors)))


def moving_balls():
    global balls_mods

    for k in range(len(balls)):
        # for each ball looking up his coords
        ball = balls[k]
        this_ball_coords = canvas_canvasov.coords(ball)

        # turning it by x by changing his score vector
        if this_ball_coords[2] >= 800:
            balls_mods[k][0] = rnd(-3, -1)
        elif this_ball_coords[0] <= 0:
            balls_mods[k][0] = rnd(1, 3)

        # turning it by y by changing his score vector
        if this_ball_coords[1] <= 0:
            balls_mods[k][1] = rnd(1, 3)
        elif this_ball_coords[3] >= 600:
            balls_mods[k][1] = rnd(-3, -1)

        # getting ball's score vector
        mod_x = balls_mods[k][0]
        mod_y = balls_mods[k][1]

        # actually moving it
        canvas_canvasov.move(ball, rnd(0, 3) * mod_x, rnd(0, 3) * mod_y)


def moving_oval():
    """ by arithmetic spiral, the angle = time * const """
    for oval in ovals:
        canvas_canvasov.move(oval, - sin(how_long_the_same_set/30) *
                             how_long_the_same_set/50,
                             - how_long_the_same_set * cos(how_long_the_same_set/30)/50)


def click(event):
    """ checking whether clicked on ball or the oval and giving meows """
    global number_of_wins

    wins_per_click = 0
    all_objects_coords = []

    for ball in balls:
        all_objects_coords.append([canvas_canvasov.coords(ball), 'ball'])

    for oval in ovals:
        all_objects_coords.append([canvas_canvasov.coords(oval), 'oval'])

    # comparing event.xy to every object coords
    for i in all_objects_coords:
        x0 = i[0][0]
        y0 = i[0][1]
        x1 = i[0][2]
        y2 = i[0][3]

        if (x0 < event.x < x1) and (y0 < event.y < y2):
            wins_per_click += 1

            # and more for the oval
            if i[1] == 'oval':
                wins_per_click += 4

    # if one click got it to more than one object
    # than it's definitely should be more meows
    number_of_wins += wins_per_click**2

    # updating score
    canvas_canvasov.delete('wins')
    canvas_canvasov.create_text(100, 100, tag='wins', text='meows: '
                                                           + str(number_of_wins))

    # if the score is big enough for best scores file
    if number_of_wins > lowest_best_score:
        name = entered_name.get()
        if name == '':
            name = 'noname'
        best_results[name] = str(number_of_wins)
        writing_scores()


def writing_scores():
    """ writing best of the best scores to the file """
    scores_table = open('scores', 'w')
    for key in best_results:
        scores_table.write(key + ' ' + best_results[key] + '\n')
    scores_table.close()


def game_core():
    """ the main function of it all, 42 btw """
    global how_long_the_same_set

    if how_long_the_same_set > 400:
        how_long_the_same_set = 0
        new_set()

    else:
        moving_balls()
        moving_oval()
        how_long_the_same_set += 1

    root.after(timer_time, game_core)


game_core()
canvas_canvasov.bind('<Button-1>', click)
root.mainloop()
