from itertools import permutations

def travelling_salesman(cost_matrix, start_city):
    n = len(cost_matrix)
    
   
    cities = [i for i in range(n) if i != start_city]
    
    min_cost = float('inf')
    optimal_path = []
    
   
    for perm in permutations(cities):
        current_cost = 0
       
        tour = [start_city] + list(perm) + [start_city]
        
        for i in range(len(tour) - 1):
            current_cost += cost_matrix[tour[i]][tour[i+1]]
        
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_path = tour
            
    return optimal_path, min_cost

if __name__ == "__main__":
   
    cost_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    starting_city = 0  
    
    path, cost = travelling_salesman(cost_matrix, starting_city)
    
    print("Optimal Path:", path)
    print("Minimum Travelling Cost:", cost)