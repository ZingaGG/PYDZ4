# Task 1

import random

a = []
b = []
c = set()

for i in range(random.randint(1,10)):
    a.append(random.randint(1,10))

for i in range(random.randint(1,10)):
    b.append(random.randint(1,10))

c = a + b

c = set(sorted(c))

print(a,b,c)