def solve_n_queens(n):
  col = set()
  pos_diag = set()  
  neg_diag = set()  

  res = []
  board = [["."] * n for _ in range(n)]

  def backtrack(r):
    if r == n:
      res.append(["".join(row) for row in board])
      return

    for c in range(n):
      if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
        continue

      col.add(c)
      pos_diag.add(r + c)
      neg_diag.add(r - c)
      board[r][c] = "Q"

      backtrack(r + 1)

      col.remove(c)
      pos_diag.remove(r + c)
      neg_diag.remove(r - c)
      board[r][c] = "."

  backtrack(0)
  return res


if __name__ == "__main__":
  n = 4
  print(f"\n--- {n}-Queens Problem Solutions ---")
  solutions = solve_n_queens(n)
  print(f"Total solutions found: {len(solutions)}\n")
  
  for idx, sol in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for row in sol:
      print(row)
    print()