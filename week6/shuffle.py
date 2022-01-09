import random

list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

for i in range(len(list) - 1, 0, -1):
    x = random.randint(0, i + 1)
    list[i], list[x] = list[x], list[i]

print(str(list))
# print(str(ranFunc(list)))