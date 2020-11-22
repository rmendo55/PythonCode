import tkinter as tk
import copy


class Nqueens:
    def __init__(self, root):
        self.root = root
        self.nQueen_list = []
        self.nQueen_solutions = []
        self.index = 0

    def create_gui(self):
        # height of screen
        height = self.root.winfo_screenheight()
        # width of screen
        width = self.root.winfo_screenwidth()
        # setting window heigt respect to computer screen
        self.root.geometry(str(width) + 'x' + str(height))

        # input Label
        label = tk.Label(self.root, text="Enter Grid Size(nxn):")
        label.grid(column=0, row=0)
        entry = tk.Entry(self.root)
        entry.grid(column=2, row=0)
        button = tk.Button(self.root, text="Generate", command=lambda: self.populateGrid(entry.get()))
        button.grid(column=0, row=2)
        self.root.mainloop()

    def populateGrid(self, entry):
        row = entry[0]  # get row
        col = entry[2]  # get column
        # empty nQueen_list
        if len(self.nQueen_list) != 0:
            self.nQueen_list = []
            self.nQueen_solutions = []
        self.populateArray(int(row), int(col))
        self.createGrid()

        if len(self.nQueen_list) != 0:
        #Display buttons for grid
        #Button to Show whole Solution
            button_solution1 = tk.Button(root, text="Show Whole Solution", command=lambda: self.showSolution())
            button_solution1.grid(column= 5, row= 0)

    def emptyArray(self):
        self.nQueen_list = []


    def populateArray(self, row, col):
        for x in range(row):
            current_row = []
            for y in range(col):
                current_row.append(0)
            self.nQueen_list.append(current_row)

    def createGrid(self):
        # start at row 5
        # start at column 5
        row = 10
        for x in range(len(self.nQueen_list)):
            row += 1
            col = 4
            for y in range(len(self.nQueen_list[0])):
                col += 1
                canvas_widget = tk.Canvas(self.root, bg="black", width=80, height=80)
                canvas_widget.grid(column=col, row=row)


    def showSolution(self):
        self.nQueens(0)
        label = tk.Label(self.root, text="Number of Solutions: " + str(len(self.nQueen_solutions)))
        label.grid(column= 10, row= 0)
        if len(self.nQueen_solutions) == 0:
            #No Solution
            print('No Solution')
        else:
            #Display buttons for grid
            #Display number of solutions and allowing user to switch back and forth with solutions
            prev_butt = tk.Button(self.root, text="Prev", command=lambda: self.showNextSolution(True, False))
            next_butt = tk.Button(root, text="Next", command=lambda: self.showNextSolution(False, True))
            label2 = tk.Label(self.root, text="Solution 1")
            label2.grid(column = 15, row = 0)
            prev_butt.grid(column=20, row=0)
            next_butt.grid(column=25, row=0)
            self.createSolutionGrid()

    def showNextSolution(self, isPrev, isNext):
        if isPrev and self.index != 0:
            self.index = self.index - 1
            label2 = tk.Label(self.root, text="Solution " + str(self.index + 1))
            label2.grid(column=15, row=0)
        elif isNext and self.index + 1 < len(self.nQueen_solutions):
            self.index = self.index + 1
            label2 = tk.Label(self.root, text="Solution " + str(self.index + 1))
            label2.grid(column=15, row=0)
        #show solution
        self.createSolutionGrid()



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
                    canvas_widget = tk.Canvas(self.root, bg="red", width=80, height=80)
                else:
                    canvas_widget = tk.Canvas(self.root, bg="black", width=80, height=80)
                canvas_widget.grid(column=col, row=row)


    #Store all possible solution to nQueen_solutions
    def nQueens(self, row):
        #base case
        if row == len(self.nQueen_list):
            #a solution exists
            list2 = copy.deepcopy(self.nQueen_list)
            self.nQueen_solutions.append(list2);
            return
        else:
            for y in range(len(self.nQueen_list[0])):
                #place queen at current row and column:y but first validate
                if not(self.validation_position(row, y)):
                    #place queen and then recurse
                    self.nQueen_list[row][y] = 1
                    self.nQueens(row + 1)
                    #when recursed back set current row and col back to 0
                    self.nQueen_list[row][y] = 0

            return

    def validation_position(self, row, col):
        #check left to right
        not_collision = False
        for x in range(len(self.nQueen_list[0])):
            if (self.nQueen_list[row][x] == 1):
                not_collision = True
                break

        #check right diagonal
        r = row
        c = col
        while (r >= 0 and c < len(self.nQueen_list[0])):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r - 1
            c = c + 1

        #check left diagonal
        r = row
        c = col
        while (r >= 0 and c >= 0):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r - 1
            c = c - 1

        #check lower right diagonal
        r = row
        c = col
        while(r < len(self.nQueen_list) and c < len(self.nQueen_list[0])):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r + 1
            c = c + 1

        #check lower left diagonal
        r = row
        c = col
        while(r < len(self.nQueen_list) and c >= 0):
            if (self.nQueen_list[r][c] == 1):
                not_collision = True
                break
            r = r + 1
            c = c - 1

        #check top to bottom
        c = col
        for x in range(len(self.nQueen_list)):
            if (self.nQueen_list[x][c] == 1):
                not_collision = True
                break

        return not_collision

# def print_2D_array(list):
#     print("Solution: ")
#     for x in range(len(list)):
#         s = ""
#         for y in range(len(list[0])):
#             s += str(list[x][y]) + " "
#         print(s)
# main()

root = tk.Tk()
n = Nqueens(root)

# Test if nQueen_list is pass by reference or pass by value
# print(n.nQueen_list)
# n.populateArray()
# print(n.nQueen_list)

n.create_gui()
# root.mainloop()
