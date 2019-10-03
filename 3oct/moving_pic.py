from math import sin, cos
from typing import Tuple, List

from graph import penSize, penColor, brushColor, moveObjectBy, changeCoords
from graph import polygon, circle, line, rectangle, point
from graph import windowSize, canvasSize, run, onTimer

Point = Tuple[float, float]
Polyline = List[Point]
DrawableObject = int
Drawing = List[DrawableObject]


def color(r: int, g: int, b: int):
    """Set color to both sources"""
    penColor(r, g, b)
    brushColor(r, g, b)


def move_by(pic: Drawing, x: int, y: int):
    """Move pic object by (x, y); pic can pe swan(), fish() and so on"""
    for obj in pic:
        moveObjectBy(obj, x, y)


def turn(points: Polyline, angle: float):
    """Turn every point in the set on certain angle"""
    out_points = []
    for pt in points:
        out_points.append((pt[0] * cos(angle) + pt[1] * sin(angle),
                           -pt[0] * sin(angle) + pt[1] * cos(angle)))
    return out_points


def reflect_offset(offset: float, reflect: bool):
    """Use it if you move a part of a figure that can be reflected"""
    return -offset if reflect else offset


def scale_reflect(points: Polyline, scale: float, reflect: bool):
    """Scale and reflect point set"""
    out_points = []
    for pt in points:
        x = 400 - pt[0] * scale if reflect else pt[0] * scale
        y = pt[1] * scale
        out_points.append(
            (x, y))
    return out_points


def poly_sr(points: Polyline, scale: float, reflect: bool):
    """Draw a scaled and reflected instance of a polygon"""
    return polygon(scale_reflect(points, scale, reflect))


def ellipse_sr(x1: int, y1: int, x2: int, y2: int, scale: float, reflect: bool):
    """Draw a scaled and reflected instance of an ellipse"""
    base = circle(0, 0, 10)
    if not reflect:
        changeCoords(base, [(x1 * scale, y1 * scale), (x2 * scale, y2 * scale)])
    else:
        changeCoords(base, [(400 - x1 * scale, y1 * scale), (400 - x2 * scale, y2 * scale)])
    return base


def line_sr(x1: int, y1: int, x2: int, y2: int, scale: float, reflect: bool):
    """Draw a scaled and reflected instance of a line"""
    return line(400 - x1 * scale, y1 * scale, 400 - x2 * scale, y2 * scale) if reflect \
        else line(x1 * scale, y1 * scale, x2 * scale, y2 * scale)


def foot(scale: float, reflect: bool):
    """The Swan's foot"""
    penSize(scale)
    # Points were selected randomly, attention
    foot_pts = [(239, 243), (230, 250), (235, 250), (245, 240), (255, 230), (250, 230), (242, 240), (247, 228),
                (242, 228), (241, 240), (240, 225), (235, 225), (239, 237), (219, 227), (217, 233)]
    return poly_sr(foot_pts, scale, reflect)


def wing(scale: float, reflect: bool):
    """The Swan's wing"""
    penSize(scale)
    # Points were selected randomly, attention
    wing_pts = [(50, 100), (40, 90), (40, 40), (10, 0), (30, 0), (100, 60), (105, 70), (100, 80), (60, 100)]
    return poly_sr(
        wing_pts, scale,
        reflect)


def swan(scale: float = 1., reflect: bool = False):
    """The Swan"""
    penSize(scale)
    penColor('black')
    brushColor('orange')
    swan_objs = [ellipse_sr(380, 110, 418, 120, scale, reflect),  # Element #0 - beak lower part
                 ellipse_sr(380, 105, 420, 115, scale, reflect),  # Element #1 - beak upper part
                 foot(scale, reflect),  # Element #2 - left foot
                 foot(scale, reflect)]  # Element #3 - right foot
    moveObjectBy(swan_objs[2], reflect_offset(14 * scale, reflect), 6 * scale)  # Move left foot to needed position
    moveObjectBy(swan_objs[3], reflect_offset(74 * scale, reflect), 6 * scale)  # Move left right to needed position
    brushColor('white')
    # Points were selected randomly, attention
    tail_pts = [(160, 125), (160, 150), (80, 163), (103, 150), (70, 141), (100, 129), (80, 110)]
    swan_objs.extend([wing(scale, reflect),  # Element #4 - left wing
                      wing(scale, reflect),  # Element #5 - right wing
                      poly_sr(tail_pts, scale, reflect)])  # Element #6 - tail
    moveObjectBy(swan_objs[4], reflect_offset(140 * scale, reflect), 7 * scale)  # Move left wing to needed position
    moveObjectBy(swan_objs[5], reflect_offset(190 * scale, reflect), 7 * scale)  # Move right wing to needed position
    penColor('white')
    swan_objs.extend([ellipse_sr(150, 100, 300, 180, scale, reflect),  # Element #7 - body
                      ellipse_sr(280, 110, 340, 140, scale, reflect),  # Element #8 - neck
                      ellipse_sr(330, 95, 390, 130, scale, reflect)])  # Element #9 - head
    brushColor('black')
    swan_objs.append(ellipse_sr(360, 102, 372, 110, scale, reflect))  # Element #10 - eye
    penSize(10 * scale)
    swan_objs.extend([line_sr(190, 160, 220, 230, scale, reflect),  # Elements ##11-16 - legs
                      line_sr(250, 160, 280, 230, scale, reflect),
                      line_sr(220, 230, 240, 240, scale, reflect),
                      line_sr(280, 230, 300, 240, scale, reflect),
                      circle({False: 220 * scale, True: 400 - 220 * scale}[reflect], 230 * scale, 1.5 * scale),
                      circle({False: 280 * scale, True: 400 - 280 * scale}[reflect], 230 * scale, 1.5 * scale)])
    return swan_objs


def fish():
    """The Fish"""
    penSize(1)
    penColor('black')
    brushColor('#9c292d')
    fish_objs = [polygon([(60, 85), (110, 93), (110, 107), (60, 115), (80, 100)]),  # Tail
                 polygon([(140, 100), (135, 70), (162, 74), (188, 68), (205, 76), (200, 100)]),  # Upper fin
                 polygon([(134, 110), (150, 110), (152, 130), (130, 127)]),  # Lower hind fin
                 polygon([(185, 110), (197, 110), (200, 128), (187, 131)])]  # Lower front fin
    brushColor('#9fbde6')
    penColor(brushColor())
    fish_objs.extend([polygon([(195, 85), (190, 115), (235, 100)]),  # Head
                      ellipse_sr(120, 80, 210, 120, 1, False),  # Body
                      polygon([(95, 91), (95, 109), (130, 113), (130, 87)])])  # Ass
    brushColor('green')
    fish_objs.append(circle(206, 96, 5))  # Eyeball
    brushColor('black')
    penColor('black')
    fish_objs.append(circle(207, 95, 2))  # Eye pupil
    return fish_objs


def bird_pts():
    """Generate a point array which can be used to draw a bird"""
    penColor('white')
    penSize(3)
    points = []
    for i in range(30):
        points.append((i - 30, 0.02 * i * (i - 30)))
    for i in range(31):
        points.append((i, 0.02 * i * (i - 30)))
    return points


def bird(scale: float = 1., angle: float = 0.):
    """Draw a scaled and turned instance of a bird"""
    pts = turn(scale_reflect(bird_pts(), scale, False), angle)
    lines = []
    for i in range(len(pts) - 1):
        lines.append(line(*pts[i], *pts[i + 1]))
        lines.append(point(*pts[1]))
    return lines


windowSize(600, 900)
canvasSize(600, 900)

# Background
color(20, 20, 180)
rectangle(0, 0, 600, 100)
color(100, 40, 210)
rectangle(0, 100, 600, 180)
color(140, 60, 200)
rectangle(0, 180, 600, 250)
color(170, 100, 170)
rectangle(0, 250, 600, 340)
color(230, 140, 170)
rectangle(0, 340, 600, 410)
color(250, 160, 50)
rectangle(0, 410, 600, 490)
color(40, 120, 150)
rectangle(0, 490, 600, 900)

# Swans
sw1 = swan(scale=0.8)
sw2 = swan(scale=0.3, reflect=True)
sw3 = swan(scale=0.5, reflect=False)
move_by(sw1, -60, 540)
move_by(sw2, 250, 470)
move_by(sw3, 200, 510)

# Fish
fish1 = fish()
fish2 = fish()
fish3 = fish()
move_by(fish1, 10, 750)
move_by(fish2, 240, 680)
move_by(fish3, 330, 620)

# Birds
bird1 = bird(scale=2, angle=0.2)
move_by(bird1, 100, 100)
move_by(bird(scale=1, angle=-0.2), 530, 130)
move_by(bird(scale=2, angle=0.1), 260, 170)
move_by(bird(scale=1, angle=-0.05), 130, 450)
move_by(bird(scale=0.5, angle=0.04), 410, 200)
move_by(bird(scale=1, angle=-0.02), 500, 210)
move_by(bird(scale=2, angle=0.26), 290, 290)
move_by(bird(scale=2.5, angle=0.3), 490, 390)
move_by(bird(scale=0.3, angle=-0.1), 50, 190)


def timerfun():
    move_by(sw1, 0.3, -0.6)
    move_by(sw2, -0.1, -0.4)
    move_by(sw3, 0.5, 0.5)
    move_by(fish1, 0.5, 0)
    move_by(fish2, 0.3, 0.05)
    move_by(fish3, 0.7, 0.2)


onTimer(timerfun, 100)

run()
