from collections import deque


def water_jug_problem(jug1_capacity, jug2_capacity, target):
  visited = set()

  queue = deque([(0, 0, [])])

  while queue:
    j1, j2, path = queue.popleft()

    if j1 == target or j2 == target:
      return path + [(j1, j2)]

    if (j1, j2) in visited:
      continue
    visited.add((j1, j2))

    current_path = path + [(j1, j2)]

    # 1. Fill Jug 1
    queue.append((jug1_capacity, j2, current_path))
    # 2. Fill Jug 2
    queue.append((j1, jug2_capacity, current_path))
    # 3. Empty Jug 1
    queue.append((0, j2, current_path))
    # 4. Empty Jug 2
    queue.append((j1, 0, current_path))
    # 5. Pour Jug 1 -> Jug 2
    pour1 = min(j1, jug2_capacity - j2)
    queue.append((j1 - pour1, j2 + pour1, current_path))
    # 6. Pour Jug 2 -> Jug 1
    pour2 = min(j2, jug1_capacity - j1)
    queue.append((j1 + pour2, j2 - pour2, current_path))

  return None


if __name__ == "__main__":
  jug1, jug2, target = 4, 3, 2
  print(f"--- Water Jug Problem (Jug1: {jug1}L, Jug2: {jug2}L, Target: {target}L) ---")
  solution = water_jug_problem(jug1, jug2, target)
  
  if solution:
    for step, state in enumerate(solution):
      print(f"Step {step}: Jug 1 = {state[0]}L, Jug 2 = {state[1]}L")
  else:
    print("No solution found.")