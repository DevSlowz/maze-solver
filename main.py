from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    

    # point1 = Point(5,10)
    # point2 = Point(20,60)

    # line = Line(Point(50, 50), Point(400, 400))

    # win.draw_line(line, "red")
    # Create some cells and draw them
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    win.wait_for_close()
main()