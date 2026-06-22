from random import shuffle, sample, random, choice

def genetic_algorithm(array_problem, pop_size=100, generations=500, mutation_rate=0.05):
    n = len(array_problem)
    def create_individual():
        cities = list(range(1, n))
        shuffle(cities)
        return [0] + cities + [0]
    
    population = [create_individual() for _ in range(pop_size)]

    def calculate_cost(route):
        cost = 0
        for i in range(len(route) - 1):
            cost += array_problem[route[i]][route[i+1]]
        return cost
    
    def crossover(parent1, parent2):
        p1_core = parent1[1:-1]
        p2_core = parent2[1:-1]

        start, end = sorted(sample(range(n-1), 2))

        child_core = [None] * (n-1)
        child_core[start:end] = p1_core[start:end]

        p2_pointer = 0
        for i in range(n-1):
            if child_core[i] is None:
                while p2_core[p2_pointer] in child_core:
                    p2_pointer += 1
                child_core[i] = p2_core[p2_pointer]
        
        return [0] + child_core + [0]

    def mutate(route):
        if random() < mutation_rate:
            idx1, idx2 = sample(range(1, n-1), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]
        
        return route
    
    best_overall_route = None
    best_overall_cost = float('inf')

    for gen in range(generations):
        scored_population = [(route, calculate_cost(route)) for route in population]

        scored_population.sort(key=lambda x: x[1])

        if scored_population[0][1] < best_overall_cost:
            best_overall_cost = scored_population[0][1]
            best_overall_route = scored_population[0][0]
        
        elite_count = int(pop_size * 0.2)
        new_population = [ind[0] for ind in scored_population[:elite_count]]

        while len(new_population) < pop_size:
            p1 = choice(scored_population[:int(pop_size*0.5)])[0]
            p2 = choice(scored_population[:int(pop_size*0.5)])[0]

            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
    
    return best_overall_route, best_overall_cost