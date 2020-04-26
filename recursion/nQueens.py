def main():
    nQueen_list = populateArray()
    list_solutions = nQueens(nQueen_list, 0)

def populateArray():
    #4x4
    return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def print_2D_array(list):
    print("Solution: ")
    for x in range(len(list)):
        s = ""
        for y in range(len(list[0])):
            s += str(list[x][y]) + " "
        print(s)

def nQueens(list, row):
    #base case
    if row == len(list):
        # #a solution exists
        print_2D_array(list)
        return
    else:
        for y in range(len(list[0])):
            #place queen at current row and column:y but first validate
            if not(validation_position(list, row, y)):
                #place queen and then recurse
                list[row][y] = 1
                nQueens(list, row + 1)
                #when recursed back set current row and col back to 0
                list[row][y] = 0

        return

def validation_position(list, row, col):
    #check left to right
    not_collision = False
    for x in range(len(list[0])):
        if (list[row][x] == 1):
            not_collision = True
            break

    #check right diagonal
    r = row
    c = col
    while (r >= 0 and c < len(list[0])):
        if (list[r][c] == 1):
            not_collision = True
            break
        r = r - 1
        c = c + 1

    #check left diagonal
    r = row
    c = col
    while (r >= 0 and c >= 0):
        if (list[r][c] == 1):
            not_collision = True
            break
        r = r - 1
        c = c - 1

    #check lower right diagonal
    r = row
    c = col
    while(r < len(list) and c < len(list[0])):
        if (list[r][c] == 1):
            not_collision = True
            break
        r = r + 1
        c = c + 1

    #check lower left diagonal
    r = row
    c = col
    while(r < len(list) and c >= 0):
        if (list[r][c] == 1):
            not_collision = True
            break
        r = r + 1
        c = c - 1

    #check top to bottom
    c = col
    for x in range(len(list)):
        if (list[x][c] == 1):
            not_collision = True
            break

    return not_collision

main()

