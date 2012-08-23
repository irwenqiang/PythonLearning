from random import random

N = 100000
count = 0

for i in range(0, N):
    x = random() * 2 - 1;
    y = random() * 2 - 1;
    if x * x + y * y < 1:
        count += 1

print 'PI is roughly ', 4.0 * count / N
