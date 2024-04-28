from tkinter import Tk, BOTH, Canvas

class Window :
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
        self.__canvas.pack(fill='both', expand=1)

        # Represents if window is running
        self.__is_runnig = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    # Redraw graphics in the window
    def redraw(self) :
        # update display without processing any other events or callbacks
        self.__root.update_idletasks()
        # Process all pending events 
        self.__root.update()


    # Set is_running to True
    def wait_for_close(self):
        # Indicate window is running
        self.__is_runnig = True

        # If the window is running draw 
        while self.__is_runnig :
            self.redraw()
        # If it is not open display message    
        print("window closed...")


    # Set running state to False
    def close(self):
        self.__is_runnig = False

