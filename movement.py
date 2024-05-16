import random
import math

def main():
    x = [random.uniform(-100, 100) for _ in range(10)]
    max_int = 1000
    t = 0
    while t < max_int:
        n = movement(x)
        if fitness(n) < fitness(x):
            x = n
        t += 1
        print("Iteration: {}, Fitness Value: {}".format(t, fitness(x)))
    print("Data:")
    print(",".join(map(str, x)))

def movement(x):
    n = x.copy()
    ind = random.randint(0, 9)
    f = -2 + random.random() * 4
    n[ind] = n[ind] + f
    if n[ind] < -100:
        n[ind] = -100
    if n[ind] > 100:
        n[ind] = 100
    return n

def fitness(x):
    return sum(i ** 2 for i in x)

if __name__ == "__main__":
    main()
