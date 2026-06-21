# Setup of Problem
from random import randint

def random_array_problem(points=5):

    if(points <= 0):
        raise ValueError("Invalid number of points")

    array = [[0 for _ in range(points)] for _ in range(points)]

    for i in range(points):
        for j in range(points):
            if i != j:
                array[i][j] = randint(1, 100)
    
    return array
