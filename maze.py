from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed

        if self._seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        # Populate every row with a column full of cells
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        # For every cell draw the cell 
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Check if the window object is None. If so, stop the function early.
        if self._win is None:
            return
        
        # Calculate the x-coordinate (x1) of the cell's top-left corner.
        # It combines the maze's left edge (self._x1) with the horizontal distance based on cell's column.
        x1 = self._x1 + i * self._cell_size_x
        
        # Calculate the y-coordinate (y1) of the cell's top-left corner.
        # It uses the maze's top edge (self._y1) and the vertical distance based on cell's row.
        y1 = self._y1 + j * self._cell_size_y
        
        # Find the x-coordinate (x2) of the cell's bottom-right corner by adding the cell's width to x1.
        x2 = x1 + self._cell_size_x
        
        # Determine the y-coordinate (y2) of the cell's bottom-right corner by adding the cell's height to y1.
        y2 = y1 + self._cell_size_y
        
        # Use the calculated coordinates to draw the cell at its designated position.
        self._cells[i][j].draw(x1, y1, x2, y2)
        
        # Update the window to reflect the newly drawn cell and potentially pause briefly to allow for animation.
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)