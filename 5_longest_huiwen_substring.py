import pysnooper

def is_huiwen_str(s):
    if s == s[::-1]:
        return True

    return False


@pysnooper.snoop()
def longestPalindrome(s):

    sub_len = 0
    str_longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if not is_huiwen_str(s[i:j]):
                continue
            if sub_len < j - i:
                sub_len = j - i
                str_longest = s[i:j]

    return str_longest


s = longestPalindrome("bb")
print(s)