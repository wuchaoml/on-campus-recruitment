# num_list = input().split('-')

# num_list.sort()

# num_total = []

# total = 1

# for i in range(1, num_list):
#     if num_list[i] = num_list[i - 1]:
#         total += 1
#     else:
#         num_total.append([num_list[i - 1], total])
#         total = 1

# sorted(num_dict, key=lambda x: x[1])

# output = ''

# compare_list = []

# for i in range(len(num_total)):
# 	if num_total[i][1]>num_total[i+1][1]:
# 		if len(compare_list)
# 		output += num_total[i][0] + '-'+num_total[i][1]
# 	else:
# 		compare_list.append(num_total[i])


k = int(input())

w = int(input())

profit_list = input().split(' ')

capital_list = input().split(' ')

for i in range(len(profit_list)):
    profit_list[i] = int(profit_list[i])
    capital_list[i] = int(capital_list[i])

profit = 0

select_list = []

for i in range(k):
    for j in range(len(capital_list)):
        if capital_list[j] <= w:
            select_list.append(j)
    profit_one = 0
    profit_index = 0
    for j in range(len(select_list)):
        if profit_one < profit_list[select_list[j]]:
            profit_one = profit_list[select_list[j]]
            profit_index = select_list[j]
    profit += profit_one
    w += profit_one
    del profit_list[profit_index]
    del capital_list[profit_index]

print(profit)
