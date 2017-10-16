# import math
# string_num = input()
# n, m = string_num.split(' ')
# n, m = int(n), int(m)
# count = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         num = math.sqrt(i * j)
#         num = num - int(num)
#         if num <= 0:
#             count += 1
# print(count)

import math
string_num = input()
n, m = string_num.split(' ')
n, m = int(n), int(m)
count = 0
list_total = []
n_max = int(math.sqrt(n))
m_max = int(math, sqrt(m))

for i in range(1, max(n, m)):
    num = math.sqrt(i)
    num = num - int(num)
    if num <= 0:
        count += 1
    list_total.append()

print(count)
