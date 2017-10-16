n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

m = int(input())

for i in range(m - 1):
    num_list.append(num_list[i])

total_list = []

for i in range(n):
    total = 0
    for j in range(i, m + i):
        total += num_list[j]
        total_list.append(total)

total_list.sort()
print(total_list[-1])
