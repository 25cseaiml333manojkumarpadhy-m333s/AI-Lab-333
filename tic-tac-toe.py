def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 9)


def check_winner(board):
  # Check all rows and columns
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
      return board[i][0]
    if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
      return board[0][i]

  # Check the diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return board[0][2]

  # Check for tie
  if all(cell != " " for row in board for cell in row):
    return "Tie"
  return None


def minimax(board, depth, is_maximizing):
  winner = check_winner(board)
  if winner == "O":  # AI wins
    return 10 - depth
  if winner == "X":  # Human wins
    return depth - 10
  if winner == "Tie":
    return 0

  if is_maximizing:
    max_eval = -float("inf")
    for r in range(3):
      for c in range(3):
        if board[r][c] == " ":
          board[r][c] = "O"
          eval = minimax(board, depth + 1, False)
          board[r][c] = " "
          max_eval = max(max_eval, eval)
    return max_eval
  else:
    min_eval = float("inf")
    for r in range(3):
      for c in range(3):
        if board[r][c] == " ":
          board[r][c] = "X"
          eval = minimax(board, depth + 1, True)
          board[r][c] = " "
          min_eval = min(min_eval, eval)
    return min_eval


def find_best_move(board):
  best_val = -float("inf")
  best_move = (-1, -1)
  for r in range(3):
    for c in range(3):
      if board[r][c] == " ":
        board[r][c] = "O"
        move_val = minimax(board, 0, False)
        board[r][c] = " "
        if move_val > best_val:
          best_val = move_val
          best_move = (r, c)
  return best_move


if __name__ == "__main__":
  print("\n--- Tic-Tac-Toe Minimax AI Demo ---")
  board = [[" " for _ in range(3)] for _ in range(3)]
  
  board[0][0] = "X"
  board[1][1] = "O"
  board[0][1] = "X"
  
  print("Current Board:")
  print_board(board)

  best_row, best_col = find_best_move(board)
  print(f"Optimal AI ('O') move calculated: Row {best_row}, Col {best_col}")