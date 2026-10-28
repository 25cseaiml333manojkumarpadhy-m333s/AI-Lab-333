def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    
    if depth == 0 or not isinstance(node, dict):
        return node

    if maximizing_player:
        max_eval = float('-inf')
        for child_name, child_node in node.items():
            eval = alpha_beta_pruning(child_node, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            
            
            if beta <= alpha:
                print(f"Pruned branch at MAX node (Beta cut-off: beta={beta}, alpha={alpha})")
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child_name, child_node in node.items():
            eval = alpha_beta_pruning(child_node, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            
        
            if beta <= alpha:
                print(f"Pruned branch at MIN node (Alpha cut-off: beta={beta}, alpha={alpha})")
                break
        return min_eval

game_tree = {
    'Branch_A': {
        'Leaf_1': 3,
        'Leaf_2': 5
    },
    'Branch_B': {
        'Leaf_3': 6,
        'Leaf_4': 9
    },
    'Branch_C': {
        'Leaf_5': 1,
        'Leaf_6': 2
    }
}

optimal_value = alpha_beta_pruning(game_tree, depth=2, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
print(f"\nOptimal value for the root node: {optimal_value}")