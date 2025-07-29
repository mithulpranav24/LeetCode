class Solution:
    def isPalindrome(self, n: int) -> bool:
        s = str(n)
        return True if s == s[::-1] else False

