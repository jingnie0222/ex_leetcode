import pysnooper

@pysnooper.snoop()
# 方法一：使用集合set求交
def longestCommonPrefix1(strs):
    for s in strs:
        if not s.isalpha():
            return ""
        if not s.islower():
            return ""

    set1 = set(strs[0])
    set2 = set(strs[1])
    common_set = set1 & set2

    for i in range(len(strs)-2):
        if len(common_set) == 0:
            return ""
        common_set = common_set & set(strs[i+2])

    return ''.join(common_set)
    for i in common_set:


def longestCommonPrefix2(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    for s in strs:
        if not s.isalpha():
            return ""
        if not s.islower():
            return ""

    ans = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(ans) and i < len(s):
            if ans[i] != s[i]:
                break
            i += 1
        ans = ans[0:i]

        if ans == "":
            return ""

    return ans






strs = ["ab","ac"]
res = longestCommonPrefix(strs)
print(res)