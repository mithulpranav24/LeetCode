class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        l1 = list(t)
        l.sort()
        l1.sort()
        if l == l1:
            return True
        return False


print(Solution().isAnagram("rat", "car"))