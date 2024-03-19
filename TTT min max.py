import random
import time


def display(grid):
    for row in range(3):
        print(" | ", end="")
        for column in range(3):
            if grid[row][column] == 0:
                print(" ", end="")
            else:
                print(grid[row][column], end="")
            print(" | ", end="")
        print("")


def available_moves(grid):
    moves = []
    for row in range(3):
        for column in range(3):
            if grid[row][column] not in ["X", "O"]:
                moves.append((row, column))
    return moves


def check_winner(grid, player):
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)) or all(
                grid[j][i] == player for j in range(3)):
            return True

    if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
        return True

    return False


def no_move_remaining(grid):
    for row in range(3):
        for column in range(3):
            if grid[row][column] not in ["X", "O"]:
                return False
    return True


def make_move(grid, row, column, player):
    if grid[row][column] not in ["X", "O"]:
        grid[row][column] = player
        return True
    return False


def evaluate(grid):
    if check_winner(grid, "O"):
        return 10
    elif check_winner(grid, "X"):
        return -10
    else:
        return 0


def minimax(grid, depth, is_maximizing):
    if check_winner(grid, "O"):
        return 10 - depth
    elif check_winner(grid, "X"):
        return -10 + depth
    elif no_move_remaining(grid):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for row in range(3):
            for column in range(3):
                if grid[row][column] not in ["X", "O"]:
                    grid[row][column] = "O"
                    eval = minimax(grid, depth + 1, False)
                    grid[row][column] = 0
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for row in range(3):
            for column in range(3):
                if grid[row][column] not in ["X", "O"]:
                    grid[row][column] = "X"
                    eval = minimax(grid, depth + 1, True)
                    grid[row][column] = 0
                    min_eval = min(min_eval, eval)
        return min_eval


def ai_move(grid):
    best_eval = float("-inf")
    best_move = None
    for row in range(3):
        for column in range(3):
            if grid[row][column] not in ["X", "O"]:
                grid[row][column] = "O"
                eval = minimax(grid, 0, False)
                grid[row][column] = 0
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, column)
    return best_move


positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pattern = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("The position for each box is as follows : ")
display(pattern)

while True:
    user_move = int(input("Enter your move position (1-9): ")) - 1
    row = user_move // 3
    column = user_move % 3
    if make_move(positions, row, column, "X"):
        display(positions)

        if check_winner(positions, "X"):
            print("Congratulations! You win!")
            break
        elif no_move_remaining(positions):
            print("It's a tie!")
            break


        print("AI player is thinking...")
        time.sleep(1)
        ai_row, ai_column = ai_move(positions)
        make_move(positions, ai_row, ai_column, "O")
        display(positions)

        if check_winner(positions, "O"):
            print("AI wins!") 
            break
        elif no_move_remaining(positions):
            print("It's a tie!")
            break
    else:
        print("Invalid move! Please enter an available position")