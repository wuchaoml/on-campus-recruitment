n = int(input())

string = input().split(' ')

price_list = []

for i in range(len(string)):
    price_list.append(int(string[i]))


m = int(input())

price = 0

for i in range(m):
    x, y = input().split(' ')
    price += price_list[int(x) - 1] * int(y)

print(price)
