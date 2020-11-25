import tkinter as tk
from tkinter.ttk import *
import copy


class Nqueens:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame2 = Frame(self.root)
        self.frame3 = Frame(self.root)
        self.frame4 = Frame(self.root)
        self.nQueen_list = []
        self.nQueen_solutions = []
        self.index = 0
        self.style = Style()

    def create_gui(self):
        height = self.root.winfo_screenheight()  # height of screen
        width = self.root.winfo_screenwidth()  # width of screen
        self.root.geometry(str(width) + 'x' + str(height))  # setting window height respect to computer screen

        label = tk.Label(self.frame, text="Enter Grid Size(nxn):")  # input Label
        label.grid(column=0, row=0)
        entry = tk.Entry(self.frame) # create textbox
        entry.grid(column=2, row=0)
        button = tk.Button(self.frame, text="Generate", command=lambda: self.populateGrid(entry.get()))  # button to start recursion
        button.grid(column=2, row=2)
        self.frame.place(relx=0.5, rely=0, anchor="n")
        self.root.mainloop()

    def populateGrid(self, entry):
        row = entry[0]  # get row
        col = entry[2]  # get column

        if len(self.nQueen_list) != 0:  # empty nQueen_list if generate button is regenerated (Empty all arrays to get new solutions)
            self.nQueen_list = []
            self.nQueen_solutions = []
        self.populateArray(int(row), int(col))  # fill nQueen_list with zero's
        # self.createGrid()                                   #create grid based on nQueen_list

        if len(self.nQueen_list) != 0:
            self.showSolution()
            # button_solution1 = tk.Button(root, text="Show Whole Solution", command=lambda: self.showSolution()) #Display buttons for grid to show the solutions to user
            # button_solution1.grid(column= 5, row= 0)
            # self.frame.place()

    def populateArray(self, row, col):
        for x in range(row):  # do a nested for loop since nQueen is based on a two d array
            current_row = []
            for y in range(col):
                current_row.append(0)
            self.nQueen_list.append(current_row)

    def createGrid(self):  # create grid
        # start at row 5
        # start at column 5
        row = 10
        for x in range(len(self.nQueen_list)):
            row += 1
            col = 4
            for y in range(len(self.nQueen_list[0])):
                col += 1
                canvas_widget = tk.Canvas(self.root, bg="black", width=80, height=80).grid(column=col, row=row)

    def showSolution(self):
        self.nQueens(0)
        if len(self.nQueen_solutions) == 0:
            print('No Solution')  #Display Label indicating there is no solution
            label = tk.Label(self.frame2, text="No Solution").grid(column=0, row=5)  # Display number of solutions
            self.frame2.place(relx=0.5, rely=0.3, anchor="center")
        else:
            label = tk.Label(self.frame3, text="Number of Solutions: " + str(len(self.nQueen_solutions))).grid(column=0,row=0)  # Display number of solutions
            self.frame2.place(relx=0.5, rely=0.3, anchor="center")
            prev_butt = tk.Button(self.frame3, text="Prev", command=lambda: self.showNextSolution(True, False)).grid(column=1, row=2) #Move to previous solution
            next_butt = tk.Button(self.frame3, text="Next", command=lambda: self.showNextSolution(False, True)).grid(column=2, row=2) #Move to next solution
            label2 = tk.Label(self.frame3, text="Solution 1").grid(column = 0, row = 2)
            self.frame3.place(relx=0.5, rely=0.2, anchor="center")
            self.createSolutionGrid()              #display grid relative to prev_butt and next_butt

    def showNextSolution(self, isPrev, isNext):
        if isPrev and self.index != 0:  # constraint to no go out of bounds where index won't ever be less than 0
            self.index = self.index - 1
            label2 = tk.Label(self.frame3, text="Solution " + str(self.index + 1))
            label2.grid(column = 0, row = 2)
        elif isNext and self.index + 1 < len(
                self.nQueen_solutions):  # constraint to avoid index out of bounds where index won't ever be greater than the length of the array
            self.index = self.index + 1
            label2 = tk.Label(self.frame3, text="Solution " + str(self.index + 1))
            label2.grid(column = 0, row = 2)
        self.createSolutionGrid()  # show solution

    def createSolutionGrid(self):
        # start at row 5
        # start at column 5
        row = 10
        for x in range(len(self.nQueen_solutions[0])):
            row += 1
            col = 4
            for y in range(len(self.nQueen_solutions[0][0])):
                col += 1
                if self.nQueen_solutions[self.index][x][y] == 1:
                    canvas_widget = tk.Canvas(self.frame4, bg="red", width=80, height=80)
                else:
                    canvas_widget = tk.Canvas(self.frame4, bg="black", width=80, height=80)
                canvas_widget.grid(column=col, row=row)
        self.frame4.place(relx=0.5, rely=0.5, anchor="center")

    # Store all possible solution to nQueen_solutions
    def nQueens(self, row):
        # base case
        if row == len(self.nQueen_list):
            # a solution exists
            list2 = copy.deepcopy(self.nQueen_list)
            self.nQueen_solutions.append(list2);
            return
        else:
            for y in range(len(self.nQueen_list[0])):
                # place queen at current row and column:y but first validate
                if not (self.validation_position(row, y)):
                    # place queen and then recurse
                    self.nQueen_list[row][y] = 1
                    self.nQueens(row + 1)
                    # when recursed back set current row and col back to 0
                    self.nQueen_list[row][y] = 0

            return

    def validation_position(self, row, col):
        # check left to right
        not_collision = False
        for x in range(len(self.nQueen_list[0])):
            if (self.nQueen_list[row][x] == 1):
                not_collision = True
                break

        # check right diagonal
        r = row
        c = col
        while (r >= 0 and c < len(self.nQueen_list[0])):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r - 1
            c = c + 1

        # check left diagonal
        r = row
        c = col
        while (r >= 0 and c >= 0):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r - 1
            c = c - 1

        # check lower right diagonal
        r = row
        c = col
        while (r < len(self.nQueen_list) and c < len(self.nQueen_list[0])):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r + 1
            c = c + 1

        # check lower left diagonal
        r = row
        c = col
        while (r < len(self.nQueen_list) and c >= 0):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r + 1
            c = c - 1

        # check top to bottom
        c = col
        for x in range(len(self.nQueen_list)):
            if (self.nQueen_list[x][c] == 1):
                not_collision = True
                break

        return not_collision


root = tk.Tk()
n = Nqueens(root)

n.create_gui()
