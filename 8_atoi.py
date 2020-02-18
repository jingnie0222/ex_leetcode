import pysnooper

limit = pow(2, 31)

def extract_int_str(str):
    if str == "":
        return 0

    res = ""
    for s in str:
        if not s.isdigit():
            break
        res += s

    return res if res else 0

def myAtoi(str):
    str = str.lstrip()  #清除空白符，例如：/n, /r, /t, ' '

    if str == "":
        return 0

    if len(str) == 1 and str.isdigit():   #2、只有一个字符，且为数字的
        return int(str)

    if str[0] == "+" or str[0] == "-":   #3、处理首字符为符号位的
        if len(str) == 1:
            return 0
        if not str[1].isdigit():
            return 0

        int_str = extract_int_str(str[1:])
        if int_str:
            if str[0] == "+":
                #return int(int_str) if int(int_str) < limit else limit-1
                return min(int(int_str), limit-1)   #使用min较好，三元表达式复杂了

            if str[0] == "-":
                return max(-int(int_str), -limit)
        return 0

    if not str[0].isdigit():  #4、首字符不是符号位，也不是数字的，这一步如果放在3前会有问题
        return 0

    int_str = extract_int_str(str)   #5、首字符是数字的，找出连续数字并返回
    if int_str:
        return min(int(int_str), limit-1)

    return 0



x = "-91283472332"
val = myAtoi(x)
print(val)


