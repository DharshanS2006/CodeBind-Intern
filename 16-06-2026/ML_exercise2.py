import random

# Simulate coin flip
def coin_flip_experiment(n):
    heads = sum(random.choice(["H", "T"]) == "H" for _ in range(n))

    return heads / n

print(f"10 flips : P(H) = {coin_flip_experiment(10):.2f}")
print(f"100 flips : P(H) = {coin_flip_experiment(100):.2f}")
print(f"1000 flips : P(H) = {coin_flip_experiment(1000):.2f}")
