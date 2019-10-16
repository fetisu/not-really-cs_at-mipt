from tkinter import Tk, Canvas, StringVar, Label, Entry, END
from random import randrange as rnd, choice
from math import cos, sin

root = Tk()
width = 800
height = 630
root.geometry(str(width)+'x'+str(height))

# the game field
canvas_canvasov = Canvas(root, bg='#cdffff', width=width, height=600)
canvas_canvasov.place(x=0, y=0)

# nice colour of bottom board
canvas_down_background = Canvas(root, bg='#AFEEFF', width=width, height=30)
canvas_down_background.place(x=0, y=600)

# entry item and setting default name
entered_name = StringVar()
name_entry = Entry(root, width=20, textvariable=entered_name, bg='#d8f7f6')
name_entry.insert(END, 'noname')
name_entry.place(x=325, y=605)

# text for bottom board
text = Label(root, text='Please, enter your name for the scores table:3',
             bg='#d8f7f6')
text.place(x=10, y=605)
text_second = Label(root, text="and do it before scoring 50, or don't do at all",
                    bg='#d8f7f6')
text_second.place(x=500, y=605)

# basic design colours
ball_colors = ['#ff9ea3', '#ffbe9e', '#ff9ed0', '#e4a3fa',
               '#e4e4b9', '#9ea9ff', '#f8d4a5', '#9ed8ff', '#b1ecd5']
oval_colors = ['#ff631c', '#cd7a00']

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
how_long_the_same_set = 1000
timer_time = 5

# explaining the game text
canvas_canvasov.create_text(150, 50, text='Hi there. This game is very simple \n'
                                          'Every click inside a ball is a meow \n'
                                          'The more meows the better')


class Ball(object):

    def __init__(self, x, y, r, color, mod_x, mod_y):
        self.mod_x = mod_x
        self.mod_y = mod_y
        self.canv = canvas_canvasov.create_oval(x - r, y - r, x + r, y + r,
                                                fill=color, width=0)

    def move(self):
        canvas_canvasov.move(self.canv, self.mod_x, self.mod_y)

    def get_x(self):
        ball_coords = canvas_canvasov.coords(self.canv)
        return ball_coords[0], ball_coords[2]

    def get_y(self):
        ball_coords = canvas_canvasov.coords(self.canv)
        return ball_coords[1], ball_coords[3]

    def should_be_turned(self):
        x, x1 = self.get_x()
        y, y1 = self.get_y()

        if x < 0 or x1 > width:
            self.mod_x = - self.mod_x

        if y < 0 or y1 > height - 30:
            self.mod_y = - self.mod_y


class Oval(object):

    def __init__(self, x, y, dx, dy, color):
        self.canv = canvas_canvasov.create_oval(x, y, x + dx, y + dy,
                                                fill=color, width=1)

    def move(self, alpha):
        canvas_canvasov.move(self.canv, - sin(alpha) * alpha * 0.3,
                             - alpha * cos(alpha) * 0.3)

    def get_x(self):
        oval_coords = canvas_canvasov.coords(self.canv)
        return oval_coords[0], oval_coords[2]

    def get_y(self):
        oval_coords = canvas_canvasov.coords(self.canv)
        return oval_coords[1], oval_coords[3]


def new_set():
    """deleting previous balls and ovals and making new ones"""
    global balls, ovals

    # clearing the field
    for ball in balls:
        canvas_canvasov.delete(ball.canv)
    for oval in ovals:
        canvas_canvasov.delete(oval.canv)

    balls = []
    ovals = []

    # new random number of balls
    for i in range(rnd(4, 12)):
        balls.append(Ball(rnd(100, 700), rnd(100, 500), rnd(20, 40),
                          choice(ball_colors), rnd(1, 5), rnd(1, 5)))

    # new zero or some ovals
    for i in range(rnd(1, 2)):
        ovals.append(Oval(rnd(100, 700), rnd(100, 500), rnd(10, 20), rnd(10, 20),
                          choice(oval_colors)))


def click(event):
    """ checking whether clicked on ball or the oval and giving meows """
    global number_of_wins

    for ball in balls:
        x, x1 = ball.get_x()
        y, y1 = ball.get_y()

        if (x <= event.x <= x1) and (y <= event.y <= y1):
            number_of_wins += 1

    for oval in ovals:
        x, x1 = oval.get_x()
        y, y1 = oval.get_y()

        if (x <= event.x <= x1) and (y <= event.y < y1):
            number_of_wins += 15

    # updating scores table
    canvas_canvasov.delete('wins')
    canvas_canvasov.create_text(100, 100, tag='wins',
                                text='meows: ' + str(number_of_wins))

    # if the score is big enough for best scores file
    if number_of_wins > lowest_best_score:
        name = entered_name.get()
        if name == '':
            name = 'noname'
        best_results[name] = str(number_of_wins)
        writing_scores()


def writing_scores():
    """ writing best of the scores to the file """
    scores_table = open('scores', 'w')
    for key in best_results:
        scores_table.write(key + ' ' + best_results[key] + '\n')
    scores_table.close()


def game_core():
    """ the main function of it all, 42 btw """
    global how_long_the_same_set

    if how_long_the_same_set > 800:
        how_long_the_same_set = 0
        new_set()

    else:
        for ball in balls:
            ball.should_be_turned()
            ball.move()

        for oval in ovals:
            oval.move(how_long_the_same_set/30)

        how_long_the_same_set += 1

    root.after(timer_time, game_core)


game_core()
canvas_canvasov.bind('<Button-1>', click)
root.mainloop()
