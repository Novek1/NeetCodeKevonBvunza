class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check cubes
        for cube_i in [0, 3, 6]:
            for cube_j in [0, 3, 6]:
                check_list = []
                i = cube_i
                for _ in range(3):
                    j = cube_j
                    for __ in range(3):
                        if board[i][j] in check_list:
                            return False
                        if board[i][j] != ".":
                            check_list.append(board[i][j])
                        j += 1
                    i += 1
             
        #check rows
        i = 0
        for _ in range(9):
            check_list = []
            j = 0
            for __ in range(9):
                if board[i][j] in check_list:
                    return False
                if board[i][j] != ".":
                    check_list.append(board[i][j])
                j += 1
            i += 1

        
        #check columns
        j = 0
        for _ in range(9):
            check_list = []
            i = 0
            for __ in range(9):
                if board[i][j] in check_list:
                    return False
                if board[i][j] != ".":
                    check_list.append(board[i][j])                
                i += 1
            j += 1

        return True
