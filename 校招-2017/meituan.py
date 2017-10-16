num = int(input())
bull_str = input().split(' ')
bull_list = []
for i in range(len(bull_list)):
    bull_list.append(int(bull_str[i]))

flag = 0
while True:
    flag += 1
    for i in range(len(bull_list)):
        if bull_list[i] == 1:
            for j in range(bull_list.index(bull_list[i]), len(bull_list)):
                if bull_list[j] == 1:
                    bull_list[j] = 0
                else:
                    bull_list = 1
            break
        if i == len(bull_list):
            flag += 1
            print('Alex' if flag % 2 == 0 else 'Bob')
            break
