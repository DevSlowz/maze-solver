from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    

    point1 = Point(5,10)
    point2 = Point(20,60)

    line = Line(point1.x, point1.y, point2.x, point2.y)

    win.draw_line(line, "red")

    win.wait_for_close()
main()