num_str = input()

one_list = []
two_list = []


def transaltion(num):
    if len(num) == 1:
        return num
    print(transaltion(num[0:-1]) + num[-1])
   # print(transaltion(num[0:-2]) + num[-2:])


transaltion(num_str)
