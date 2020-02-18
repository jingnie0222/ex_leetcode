class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        new_int = int(str(x)[::-1])
        return True if new_int == x else False