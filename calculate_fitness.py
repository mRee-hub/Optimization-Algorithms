#Bu kod (-5,5) aralığında random olarak verilen 5 adet değerin karelerinin toplamını hesaplar.

import random

def Calculate(data):
    result = 0
    for value in data :
        result += value * value
    return result

def main():
    X = [0] * 5
    for i in range(len(X)):
        X[i] = 5 - random.randint(0, 10)
        print(f"X[x{i+1}] = {X[i]}")
    obj_value = Calculate(X)
    print("Amaç fonksiyon değeri:",obj_value)
    
if __name__ == "__main__":
    main()
