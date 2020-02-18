import pysnooper

d = {1000:'M',
     900:'CM',
     500:'D',
     400:'CD',
     100:'C',
     90:'XC',
     50:'L',
     40:'XL',
     10:'X',
     9:'IX',
     5:'V',
     4:'IV',
     1:'I'}

@pysnooper.snoop()
def intToRoman(num):

    res = ""

    while num > 0:
        for i in d:
            if num >= i:
                num = num - i
                res += d[i]
                break  #一次计算之后要跳出重新计算，反例：20（正确：XX，错误：XIXI）

    return res

num = 1994
res = intToRoman(num)
print(res)
