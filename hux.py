import random

def hux_crossover(parent1, parent2):
    if len(parent1) != len(parent2):
        raise ValueError("Parent bireylerin uzunlukları eşit olmalıdır.")
    
    child1 = []
    child2 = []
    
    for i in range(len(parent1)):
        if parent1[i] != parent2[i]:
            if random.random() < 0.5:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])
        else:
            child1.append(parent1[i])
            child2.append(parent2[i])
    
    return child1, child2

# Örnek kullanım
parent1 = [1, 0, 1, 0, 1]
parent2 = [0, 1, 0, 1, 0]

child1, child2 = hux_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
