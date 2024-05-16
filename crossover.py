import random

def crossover(parent1, parent2):
    
    crossover_point = random.randint(0, min(len(parent1), len(parent2)) - 1)

    child1 = []
    child2 = []

    child1.extend(parent1[:crossover_point])
    child1.extend(parent2[crossover_point:])
    
    child2.extend(parent2[:crossover_point])
    child2.extend(parent1[crossover_point:])
    
    print("CrossOver Point :", crossover_point)
    
    return child1, child2

parent1 = [1, 2, 3, 4, 5]
parent2 = [6, 7, 8, 9, 10]

child1, child2 = crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)