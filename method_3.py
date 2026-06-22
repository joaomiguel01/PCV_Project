def bellman_held_karp(array_problem):
    n = len(array_problem)
    memo = {}

    def tsp_dp(mask, u):
        if mask == (1 << n) - 1:
            return array_problem[u][0], [0]
        
        if (mask, u) in memo:
            return memo[(mask, u)]
        
        min_cost = float('inf')
        best_next_path = []

        for v in range(n):
            if not (mask & (1 << v)):
                cost_to_v, path_from_v = tsp_dp(mask | (1 << v), v)
                total_cost = array_problem[u][v] + cost_to_v

                if total_cost < min_cost:
                    min_cost = total_cost
                    best_next_path = [v] + path_from_v
        
        memo[(mask, u)] = (min_cost, best_next_path)
        return min_cost, best_next_path
    
    total_problem_cost, remainig_path = tsp_dp(1, 0)

    complete_route = [0] + remainig_path
    return complete_route, total_problem_cost