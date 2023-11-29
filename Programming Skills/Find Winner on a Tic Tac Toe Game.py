class Solution(object):
    def tictactoe(self, moves):
        grid = [[' ' for _ in range(3)] for _ in range(3)]

        def check_winner(player):
            for i in range(3):
                if all(grid[i][j] == player for j in range(3)):
                    return True
                if all(grid[j][i] == player for j in range(3)):
                    return True
            if grid[0][0] == grid[1][1] == grid[2][2] == player:
                return True
            if grid[0][2] == grid[1][1] == grid[2][0] == player:
                return True
            return False

        for i, (row, col) in enumerate(moves):
            if i % 2 == 0:  # Player A's turn (even moves)
                grid[row][col] = 'X'
                if check_winner('X'):
                    return 'A'
            else:  # Player B's turn (odd moves)
                grid[row][col] = 'O'
                if check_winner('O'):
                    return 'B'

        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'
