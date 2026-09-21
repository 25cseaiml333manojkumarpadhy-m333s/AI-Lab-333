def minimax(depth, node, maximizing):
    
    if depth == 0:
        return node

    if maximizing:
        return max(
            minimax(depth - 1, node[0], False),
            minimax(depth - 1, node[1], False)
        )
    else:
        return min(
            minimax(depth - 1, node[0], True),
            minimax(depth - 1, node[1], True)
        )

tree = [3, 5, 2, 9]

result = max(min(tree[0], tree[1]), min(tree[2], tree[3]))

print("Best value:", result)