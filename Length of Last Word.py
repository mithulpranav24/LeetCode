class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1]) if 1 <= len(s[-1]) <=1000 else None
