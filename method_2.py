def nearest_neighbor(array_problem):
    n = len(array_problem)
    visited = set([0])
    route = [0]
    total_cost = 0
    current_city = 0

    for i in range(n-1):
        next_city = None
        min_cost = float('inf')

        for candidate in range(n):
            if candidate not in visited:
                cost = array_problem[current_city][candidate]
                if cost < min_cost:
                    min_cost = cost
                    next_city = candidate
        
        visited.add(next_city)
        route.append(next_city)
        total_cost += min_cost
        current_city = next_city
    
    total_cost += array_problem[current_city][0]
    route.append(0)

    return route, total_cost
