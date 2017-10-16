string = input()

output_list = []

num = 0
output = ''

while True:
    if string[num].isalpha():
        if string[num] == 'R' and string[num+1] == 'E' and string[num+2] =='D': 
            num +=3
            continue
        if len(output)!=0:
            output_list.append(output)
            output = ''
    else:
        output+=string[num]
    num +=1
    if num==len(string)-1:
        break

output_num = 0

if len(output_list) == 0:
    print(-1)
else:  
    for i in range(len(output_list)):
        if int(output_list[i])>output_num:
            output_num = int(output_list[i])
    print(output_num)


