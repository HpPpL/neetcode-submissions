class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRows(board) and self.isValidColumns(board) and self.isValidSquares(board)

    def isValidRows(self, board: List[List[str]]) -> bool:
        for row in board:
            print(row)
            row = [symb for symb in row if symb != "."]
            if len(row) != len(set(row)):
                return False
        return True

    def isValidColumns(self, board: List[List[str]]) -> bool:
        return self.isValidRows(zip(*board))

    def isValidSquares(self, board: List[List[str]]) -> bool:
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
