class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        l = word[0]
        if l.isupper() and word[1:].islower():
            return True
        return False

print(Solution().detectCapitalUse("CRithan"))

            
        