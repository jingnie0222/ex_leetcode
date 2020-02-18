
#检查一个字符串是否有重复字符，我们可以使用集合。
# 我们遍历字符串中的所有字符，并将它们逐个放入 set 中。在放置一个字符之前，我们检查该集合是否已经包含它。如果包含，我们会返回 false。循环结束后，我们返回 true
def check_unique_string(str):
    if len(str) < 2:
        return True

    s = set()
    for i in str:
        if i in s:
            return False
        s.add(i)

    return True


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_len = 0
        for i in range(0, len(s)):
            for j in range(i+1, len(s)):
                if not check_unique_string(s[i:j+1]):
                    continue

                if sub_len < j+1-i:
                    sub_len = j+1-i

        return sub_len

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        start = 0
        end = 0
        StrSet = set()
        while start < len(s) and end < len(s):
            StrLen = len(StrSet)
            StrSet.add(s[end])
            if not StrLen == len(StrSet):
                end += 1
                ans = max(ans, end - start)
            else:
                StrSet.remove(s[start])
                start += 1
        return ans





