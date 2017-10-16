'''幂运算的一些有趣的性质 a^b = c^d，找出1<=a,b,c,d<=n中满足这个性质的式子有多少个'''
# 当n=2时：1…^1=1;1^1=1^2;1^2=1^1;1^2=1^2;2;2^1=2^1;2^2=2^2;共有六

n = int(input())

total = 0
total_list = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total_list.append(i**j)

total_list.sort()
num = 1

for i in range(1, len(total_list)):
    if total_list[i] == total_list[i - 1]:
        num = num + 1
    else:
        total = total + num + num * (num - 1)
        num = 1
total = total + num + num * (num - 1)

print(total % 100000007)
