class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(num, rows, cols):
            for i in range(9):
                if board[rows][i] == num or board[i][cols] == num or board[3 * (rows // 3) + i // 3][3 * (cols // 3) + i % 3] == num:
                    return False
            return True
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(num, r, c):
                                board[r][c] = num
                                print("Placing", num, "at position", (r, c))  # Debug print
                                if solve():
                                    return True
                                board[r][c] = "."
                                print("Backtracking from position", (r, c))  # Debug print
                        return False
            return True
        
        solve()