def dfs_recursive(graph, current_node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()

    if traversal_order is None:
        traversal_order = []
    visited.add(current_node)
    traversal_order.append(current_node)


    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)

    return traversal_order

if __name__ == "__main__":

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
    }

    result = dfs_recursive(graph, "A")
    print("Recursive DFS Traversal:")
    print(" -> ".join(result))