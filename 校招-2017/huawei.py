one_start = input().split('.')
one_end = input().split('.')
two_start = input().split('.')
two_end = input().split('.')

flag = 'No Overlap IP'

for i in range(4):
    if two_start[i] > one_end[i]:
        break
    elif two_start[i] < one_end[i]:
        flag = 'Overlap IP'
        break
    else:
        if i == 3:
            flag = 'Overlap IP2'
        continue

print(flag)
