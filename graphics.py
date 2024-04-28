from tkinter import Tk, BOTH, Canvas

class window :
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Create root widget 
        self.__root = Tk()
        # Set title of root widget
        self.__root.title = ("Maze Solver") 

        # Create canvas
        self.__canvas = Canvas(self.__root, bg="white" ,width=width, height=height)
        # Pack the canvas to fill the window and expand if the window is resized
        self.canvas.pack(fill='both', expand=1)

        # Represents if window is running
        self.is_runnig = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    # Redraw graphics in the window
    def redraw(self) :
        # update display without processing any other events or callbacks
        self.root.update_idletasks()
        # Process all pending events 
        self.root.update()