# Task 1

# import random

# a = []
# b = []
# c = set()

# for i in range(random.randint(1,10)):
#     a.append(random.randint(1,10))

# for i in range(random.randint(1,10)):
#     b.append(random.randint(1,10))

# c = a + b

# c = set(sorted(c))

# print(a,b,c)

# Task 2

# import random

# Bush = int(input("Enter N = "))
# arr = []
# for i in range(Bush):
#     arr.append(random.randint(1,10))

# print(arr)

# arr_count = []
# for i in range(len(arr)-1):
#     arr_count.append(arr[i-1] + arr[i] + arr[i+1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# print(arr[-2], arr[-1], arr[0])
# print(arr_count)
# print(max(arr_count))
