from tkinter import Tk, BOTH, Canvas

class window :
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Create root widget 
        root = Tk()
        # Set title of root widget
        root.title = ("Maze Solver") 

        # Create canvas
        canvas = Canvas()
        canvas.pack()

        # Represents if window is running
        is_runnig = False