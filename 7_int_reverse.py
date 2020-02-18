import pysnooper

@pysnooper.snoop()
def reverse(x):
    limit = pow(2, 31)
    int_str = str(x)
    new_int_str = ""

    if int_str[0] == "+" or int_str[0] == "-":
        new_int_str = int_str[-1:0:-1]
        if int_str[0] == "+" and int(new_int_str) < limit:
            return int(new_int_str)
        elif int_str[0] == "-" and int(new_int_str) <= limit:
            return -int(new_int_str)
        else:
            return 0


    new_int_str = int_str[::-1]
    if int(new_int_str) < limit:
        return int(new_int_str)

    return 0


x = -2147483648
res = reverse(x)
print(res)