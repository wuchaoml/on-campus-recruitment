string = input()

input_list = string.split(',')

n = int(input_list[0].split('=')[1])

num_list = []

for i in range(1, len(input_list)):
    num_list.append(int(i.split('=')[1]))
