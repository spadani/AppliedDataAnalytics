import random


num_trials = 1000000
num_hits = 0

for i in range(num_trials):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if (x < 0 and y < 0) or (x > 0 and y > 0 and y/x < 1):
        num_hits += 1
        print(x)

probability = num_hits / num_trials

print("The probability is", probability)
