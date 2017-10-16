input_string = input().split(';')
input_list = []
for i in range(input_string):
    one_list = input_string[i].split(',')
    input_list.append(one_list)

while True:
    if input_list[0][0] != '1':
        print('incorrect data')
        break

input_list = sorted(input_list, key=lambda x: x[2])

out_list = []
out_list = input_list[0:1]
while True:
    for i in input_list:
        if i[]


def digui()
