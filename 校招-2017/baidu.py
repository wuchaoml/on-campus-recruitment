nhorror = int(input())
nscifi = int(input())
amount = int(input())
nhorror_list = []
nscifi_list = []
for i in range(nhorror):
    nhorror_input = input()
    star, money = nhorror_input.split(' ')
    star, money = int(star), int(money)
    money_one = money / star
    nhorror_list.append((i, money_one, money, star, 1))

for i in range(nscifi):
    nscifi_input = input()
    star, money = nscifi_input.split(' ')
    star, money = int(star), int(money)
    money_one = money / star
    nscifi_list.append((i, money_one, money, star, 2))

nhorror_list = sorted(nhorror_list, key=lambda item: item[1])
nscifi_list = sorted(nscifi_list, key=lambda item: item[1])
total_list = nhorror_list + nscifi_list
total_list = sorted(total_list, key=lambda item: item[1])
star_total = 0
total_money = 0

if (nhorror_list[0][2] + nscifi_list[0][2]) > amount:
    total_money = -1
else:
    total_star = nhorror_list[0][3] + nscifi_list[0][3]
    total_money = nhorror_list[0][2] + nscifi_list[0][2]
    total_list.remove(nhorror_list[0])
    total_list.remove(nscifi_list[0])
for i in total_list:
    if (total_money + i[2]) <= amount:
        total_star += i[3]
    else:
        break

print(total_star)
