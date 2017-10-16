num = int(input())

name_dict = {}
for i in range(num):
    name = input()
    name_dict[name] = [0, 0, 0]

for i in range(num * (num - 1) // 2):
    name_score = input()
    name, score = name_score.split(' ')
    name1, name2 = name.split('-')
    score1, score2 = score.split(':')
    score1, score2 = int(score1), int(score2)
    if score1 > score2:
        name_dict[name1][0] += 3
        ball_1_add = score1 - score2
        name_dict[name1][1] += ball_1_add
        name_dict[name1][2] += score1
        name_dict[name2][2] += score2

    elif score1 == score2:
        name_dict[name1][0] += 1
        name_dict[name2][0] += 1
        name_dict[name1][2] += score1
        name_dict[name2][2] += score2
    else:
        name_dict[name2][0] += 3
        ball_2_add = score2 - score1
        name_dict[name2][1] += ball_1_add
        name_dict[name1][2] += score1
        name_dict[name2][2] += score2

name_list = []

for key, value in name_dict.items():
    string = str(value[0]) + str(value[1]) + str(value[2])
    name_list.append([key, string])

name_list = sorted(name_list, key=lambda x: x[1], reverse=True)
name_list = name_list[0:int(num // 2)]
name_list = sorted(name_list, key=lambda x: x[0])
print(num // 2)
for i in name_list:
    print(i[0])
