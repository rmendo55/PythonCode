class Solution(object):
    def isValidSudoku(self, board):
        if self.checkColumns(board) and self.checkRow(board):
            isValid = True
            #0-2
            set = 0
            count = 0
            col = 0
            row = 0
            arr = []
            while set != 3:
                current = board[row][col]
                if arr.__contains__(current):
                    isValid = False
                    break
                if current != '.':
                    arr.append(current)
                col = col + 1
                if col == 3:
                    col = 0
                    row = row + 1
                count = count + 1

                if count == 9:
                    arr = []
                    set = set + 1
                    count = 0

            #3-5
            set = 0
            col = 3
            row = 0
            while set != 3:
                current = board[row][col]
                if arr.__contains__(current):
                    isValid = False
                    break
                if current != '.':
                    arr.append(current)
                col = col + 1
                if col == 6:
                    col = 3
                    row = row + 1
                count = count + 1

                if count == 9:
                    arr = []
                    set = set + 1
                    count = 0
            #6-8
            set = 0
            col = 6
            row = 0
            while set != 3:
                current = board[row][col]
                if arr.__contains__(current):
                    isValid = False
                    break
                if current != '.':
                    arr.append(current)
                col = col + 1
                if col == 9:
                    col = 6
                    row = row + 1
                count = count + 1

                print(arr)
                if count == 9:
                    arr = []
                    set = set + 1
                    count = 0

            return isValid
        else:
            return False



    def checkColumns(self, board):
        isValid = True
        for i in range(len(board)):
            arr = []
            for j in range(len(board[i])):
                current = board[i][j]
                if arr.__contains__(current):
                    isValid = False
                    break
                if current != '.':
                    arr.append(current)

        return isValid

    def checkRow(self, board):
        isValid = True
        col = 0
        row = 0
        arr = []
        while col != 9:
            current = board[row][col]
            if arr.__contains__(current):
                isValid = False
                break
            if current != ".":
                arr.append(current)
            row = row + 1
            if row == 9:
                arr = []
                row = 0
                col = col + 1

        return isValid


solution = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(board))
