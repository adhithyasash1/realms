def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column or diagonals
        for i in range(row):
            if board[i][col] == 1 or \
               (col - (row - i) >= 0 and board[i][col - (row - i)] == 1) or \
               (col + (row - i) < n and board[i][col + (row - i)] == 1):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append([row[:] for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    
    solutions = []
    board = [[0] * n for _ in range(n)]
    backtrack(0)
    
    return solutions

def print_solutions(solutions):
    for sol_num, solution in enumerate(solutions, start=1):
        print(f"Solution {sol_num}:")
        for row in solution:
            print(' '.join('Q' if val else '.' for val in row))
        print()

# Example usage for 8-Queens problem
n = 8
solutions = solve_n_queens(n)
print_solutions(solutions)
