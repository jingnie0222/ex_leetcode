import pysnooper
d = {'M':1000,
     'CM':900,
     'D':500,
     'CD':400,
     'C':100,
     'XC':90,
     'L':50,
     'XL':40,
     'X':10,
     'IX':9,
     'V':5,
     'IV':4,
     'I':1}

#@pysnooper.snoop()
def romanToInt(s):

    i = 0
    res = 0

    while i < len(s):
        if s[i:i+2] in d:
            res += d[s[i:i+2]]
            i += 2
            continue
        if s[i] in d:
            res += d[s[i]]
            i += 1
            continue

    return res

roman = "MCMXCIV"
res = romanToInt(roman)
print(res)