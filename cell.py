
from graphics import Point, Line

class Cell :

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

        
    def draw(self, x1, y1, x2, y2):
        # Set the coordinates for the rectangle
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Draw the left wall if it exists
        if self.has_left_wall:
            # Create a line from the top left to the bottom left of the rectangle
            line = Line(Point(x1, y1), Point(x1, y2))
            # Draw the line on the window
            self._win.draw_line(line)

        # Draw the top wall if it exists
        if self.has_top_wall:
            # Create a line from the top left to the top right of the rectangle
            line = Line(Point(x1, y1), Point(x2, y1))
            # Draw the line on the window
            self._win.draw_line(line)

        # Draw the right wall if it exists
        if self.has_right_wall:
            # Create a line from the top right to the bottom right of the rectangle
            line = Line(Point(x2, y1), Point(x2, y2))
            # Draw the line on the window
            self._win.draw_line(line)

        # Draw the bottom wall if it exists
        if self.has_bottom_wall:
            # Create a line from the bottom left to the bottom right of the rectangle
            line = Line(Point(x1, y2), Point(x2, y2))
            # Draw the line on the window
            self._win.draw_line(line)

    # Draw a path between 2 cells
    def draw_move(self, to_cell, undo=False):
        # Calculate the center of the current cell
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        # Calculate the center of the target cell
        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        # Set the fill color to red by default
        fill_color = "red"
        # If the undo flag is set, change the fill color to gray
        if undo:
            fill_color = "gray"

        # Create a line from the center of the current cell to the center of the target cell
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        # Draw the line with the specified fill color
        self._win.draw_line(line, fill_color)


        
        
