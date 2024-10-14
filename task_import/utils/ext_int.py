

def ext_num(string):
    nums =[]

    for char in string:
        if char.isnumeric():
            num = int(char)
            nums.append(num)

    return nums