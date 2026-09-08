class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set) # Initialise empty hashsets
        for r in range(9):
            for c in range(9):
                val = board[r][c] # get current board position value
                if val == '.':
                    continue
                if val in cols[c] or val in rows[r] or val in squares[(r//3, c//3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[r//3, c//3].add(val)
        return True