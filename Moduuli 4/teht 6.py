import random
N = int(input("How many random points to generate?: "))
n = 0
q = 0
while q < N:
    y = random.uniform(-1, 1)
    x = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    q += 1
pi = 4 * n / N
print("Approximation of pi:", pi)