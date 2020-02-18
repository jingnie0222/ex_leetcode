import pysnooper

dict_num_to_letter = {
    '2': list("abc"),
    '3': list("def"),
    '4': list("ghi"),
    '5': list("jkl"),
    '6': list("mno"),
    '7': list("pqrs"),
    '8': list("tuv"),
    '9': list('wxyz')
    }

@pysnooper.snoop()
def letterCombinations1(digits):
    if len(digits) == 0:
        return []

    for i in digits:
        if int(i) not in range(2,10):
            return []

    if len(digits) == 1:
        return dict_num_to_letter[digits[0]]

    res = ['']
    for i in digits:
        res = [x+y for x in res for y in dict_num_to_letter[i]]  #注意这里列表生成式的使用

    return res

#方法二：递归法，实质和方法一一样
def letterCombinations2(digits):
    if len(digits) == 0:
        return []

    for i in digits:
        if int(i) not in range(2,10):
            return []

    if len(digits) == 1:
        return dict_num_to_letter[digits[0]]

    n = len(digits)

    return [x+y for x in letterCombinations2(digits[0:n-1]) for y in dict_num_to_letter[digits[n-1]] ]





digits = "23"
res = letterCombinations2(digits)
print(res)