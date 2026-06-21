import itertools
def brute_force(array_problem):
    n = len(array_problem)
    cities = list(range(1, n))

    minor_cost = float('inf')
    best_route = []

    for perm in itertools.permutations(cities):
        current_cost = 0
        current_city = 0 # First city of array

        for next_city in perm:
            current_cost += array_problem[current_city][next_city] # Sum costs
            current_city = next_city # Next city
        
        current_cost += array_problem[current_city][0]

        if current_cost < minor_cost:
            minor_cost = current_cost
            best_route = [0] + list(perm) + [0] # Complete path
    
    return best_route, minor_cost