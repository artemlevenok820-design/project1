import random

while True:
    n = random.randint(1, 100)
    attempts = 0
    
    while True:
        g = int(input("Число: "))
        attempts += 1
        
        if g == n:
            print(f"Угадал! Попыток: {attempts}")
            break
            
        print("Больше" if g < n else "Меньше")
        
    if input("Еще раз? (да/нет): ").lower() not in ("да", "д", "y", "yes"):
        break