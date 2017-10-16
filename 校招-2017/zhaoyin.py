password = input()
digit_flag = 1
big_alphabet = 1
small_alphabet = 1
total = 0
repe_num = 1

for i in range(len(password)):
    if password[i].isdigit():
        digit_flag = 0
    if password[i].isalpha():
        if password[i].islower():
            small_alphabet = 0
        else:
            big_alphabet = 0
        if password[i] == password[i - 1]:
            repe_num += 1
        else:
            total = total + repe_num // 3

if len(password) < 6:
    if total < (6 - len(password)):
        total = 6 - len(password)
elif len(password) > 20:
    total = total + len(password) - 20
else:
    if total == 0:
        total = total + digit_flag + big_alphabet + small_alphabet

print(total)
