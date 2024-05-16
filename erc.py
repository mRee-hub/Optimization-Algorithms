import random

def edge_recombination_crossover(parent1, parent2):
    if len(parent1) != len(parent2):
        raise ValueError("Parent bireylerin uzunlukları eşit olmalıdır.")
    
    # Komşuluk listelerini oluşturma
    neighbor_lists = {}
    for i in range(len(parent1)):
        neighbor_lists[parent1[i]] = [parent1[(i-1)%len(parent1)], parent1[(i+1)%len(parent1)]]
        neighbor_lists[parent2[i]] = [parent2[(i-1)%len(parent2)], parent2[(i+1)%len(parent2)]]
    
    # Başlangıç düğümlerini seçme
    current_node = random.choice(parent1)
    child = [current_node]
    
    # Çocuk bireyi oluşturma
    while len(child) < len(parent1):
        neighbors = neighbor_lists[current_node]
        candidate_nodes = [node for node in neighbors if node not in child]
        if candidate_nodes:  # Eğer aday düğüm varsa
            current_node = min(candidate_nodes, key=lambda x: len(neighbor_lists[x]))
            child.append(current_node)
        else:  # Eğer aday düğüm yoksa
            candidate_nodes = [node for node in parent1 if node not in child]
            current_node = random.choice(candidate_nodes)
            child.append(current_node)
    
    return child

# Örnek kullanım
parent1 = [1, 2, 3, 4, 5]
parent2 = [2, 4, 1, 5, 3]

child = edge_recombination_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child:", child)