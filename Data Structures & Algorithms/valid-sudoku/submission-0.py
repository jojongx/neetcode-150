class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this is ugly I know
        for row in board:
            cnt = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for col in row:
                if col != ".":
                    cnt[col] += 1
                    if cnt[col] > 1:
                        return False

        for col in range(len(board[0])):
            cnt = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for row in range(len(board)):
                if board[row][col] != ".":
                    cnt[board[row][col]] += 1
                    if cnt[board[row][col]] > 1:
                        return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                cnt = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
                for i in range(3):
                    for j in range(3):
                        row = box_row + i
                        col = box_col + j
                        if board[row][col] != ".":
                            cnt[board[row][col]] += 1
                            if cnt[board[row][col]] > 1:
                                return False
                    
        return True